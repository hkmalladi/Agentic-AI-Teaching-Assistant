"""
Step 4: Single Tool - Function Calling

This demonstrates how to give the AI a tool (function) it can use.
The AI will decide when to call the function based on the user's request.
"""

import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    GPT4_DEPLOYMENT_NAME
)


# ============================================================================
# DEFINE THE TOOL (FUNCTION)
# ============================================================================

def generate_quiz(topic, num_questions=5):
    """
    Generate a quiz on a given topic
    
    This is a mock function. In a real app, this might:
    - Query a database
    - Use another AI model
    - Generate questions algorithmically
    
    Args:
        topic: The subject for the quiz
        num_questions: Number of questions to generate
    
    Returns:
        JSON string with quiz questions
    """
    # Mock quiz generation
    questions = []
    for i in range(num_questions):
        questions.append(f"Question {i+1} about {topic}: [Sample question here]")
    
    return json.dumps({
        "topic": topic,
        "num_questions": num_questions,
        "questions": questions
    })


# ============================================================================
# DEFINE THE TOOL SPECIFICATION
# ============================================================================

# This tells the AI about the function
tools = [
    {
        "type": "function",
        "function": {
            "name": "generate_quiz",
            "description": "Generate a quiz on a specific topic with a given number of questions",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The topic for the quiz (e.g., 'Python basics', 'World War II')"
                    },
                    "num_questions": {
                        "type": "integer",
                        "description": "Number of questions to generate",
                        "default": 5
                    }
                },
                "required": ["topic"]
            }
        }
    }
]


def main():
    print("="*70)
    print("STEP 4: SINGLE TOOL (FUNCTION CALLING)")
    print("="*70)
    print()
    
    # Initialize client
    print("📡 Initializing client...")
    client = AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
    )
    print("✅ Ready!")
    print()
    
    # Show available tools
    print("🔧 Available Tools:")
    print(f"  - {tools[0]['function']['name']}: {tools[0]['function']['description']}")
    print()
    
    # Create messages
    messages = [
        {
            "role": "system",
            "content": "You are a helpful teaching assistant. When users ask for quizzes, use the generate_quiz function."
        },
        {
            "role": "user",
            "content": "Can you create a quiz on quantum physics with 15 questions?"
        }
    ]
    
    print("👤 Student: Can you create a quiz on quantum physics with 15 questions?")
    print()
    
    # ========================================================================
    # STEP 1: Send request with tools
    # ========================================================================
    print("🚀 Sending request to AI (with tools available)...")
    print()
    
    response = client.chat.completions.create(
        model=GPT4_DEPLOYMENT_NAME,
        messages=messages,
        tools=tools,  # ⭐ Provide the tools
        tool_choice="auto"  # Let AI decide when to use them
    )
    
    response_message = response.choices[0].message
    
    # ========================================================================
    # STEP 2: Check if AI wants to call a function
    # ========================================================================
    if response_message.tool_calls:
        print("🤖 AI decided to use a tool!")
        print()
        
        # Add AI's response to messages
        messages.append(response_message)
        
        # Process each tool call
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            print(f"📞 Function Call: {function_name}")
            print(f"📋 Arguments: {json.dumps(function_args, indent=2)}")
            print()
            
            # ================================================================
            # STEP 3: Execute the function
            # ================================================================
            print(f"⚙️  Executing {function_name}...")
            
            if function_name == "generate_quiz":
                function_response = generate_quiz(
                    topic=function_args.get("topic"),
                    num_questions=function_args.get("num_questions", 5)
                )
            
            print(f"✅ Function executed!")
            print(f"📤 Result: {function_response[:100]}...")
            print()
            
            # ================================================================
            # STEP 4: Send function result back to AI
            # ================================================================
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response
            })
        
        # ================================================================
        # STEP 5: Get final response from AI
        # ================================================================
        print("🚀 Sending function results back to AI...")
        print()
        
        final_response = client.chat.completions.create(
            model=GPT4_DEPLOYMENT_NAME,
            messages=messages
        )
        
        final_message = final_response.choices[0].message.content
        
        print("="*70)
        print("FINAL RESPONSE:")
        print("="*70)
        print()
        print(f"🤖 AI: {final_message}")
        print()
        
    else:
        # AI didn't use a tool
        print("🤖 AI responded without using tools:")
        print(response_message.content)
        print()
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    print("="*70)
    print("SUMMARY:")
    print("="*70)
    print("✅ We defined a tool (generate_quiz)")
    print("✅ We told the AI about the tool")
    print("✅ AI decided to use the tool")
    print("✅ We executed the function")
    print("✅ AI formatted the results nicely")
    print()
    print("This is how AI can use external functions!")
    print()


if __name__ == "__main__":
    main()
    print("Next: Try Step 5 to see multiple tools!")
    print("  cd ../05_multiple_tools")
    print("  python multiple_tools.py")
    print()

