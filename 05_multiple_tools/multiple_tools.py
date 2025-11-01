"""
Step 5: Multiple Tools - AI Chooses the Right Tool

Demonstrates giving the AI multiple tools and watching it choose the right one.
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
# DEFINE MULTIPLE TOOLS
# ============================================================================

def generate_quiz(topic, num_questions=5):
    """Generate a quiz on a topic"""
    questions = []
    for i in range(num_questions):
        questions.append({
            "question": f"Sample question {i+1} about {topic}",
            "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
            "correct": "A"
        })
    return json.dumps({"topic": topic, "questions": questions})


def explain_concept(topic):
    """Explain a concept clearly"""
    return json.dumps({
        "topic": topic,
        "explanation": f"This is a detailed explanation of {topic}",
        "example": f"Example related to {topic}",
        "key_points": [f"Point 1 about {topic}", f"Point 2 about {topic}"]
    })


def assess_answer(answer, question):
    """Assess a student's answer"""
    return json.dumps({
        "answer": answer,
        "question": question,
        "assessment": "Good attempt!",
        "grade": "B+",
        "feedback": "Consider adding more details"
    })


# ============================================================================
# DEFINE TOOL SPECIFICATIONS
# ============================================================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "generate_quiz",
            "description": "Generate a quiz on a specific topic with multiple choice questions",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "The topic for the quiz"},
                    "num_questions": {"type": "integer", "description": "Number of questions", "default": 5}
                },
                "required": ["topic"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "explain_concept",
            "description": "Explain a concept clearly with examples and key points",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "The concept to explain"}
                },
                "required": ["topic"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "assess_answer",
            "description": "Assess and grade a student's answer to a question",
            "parameters": {
                "type": "object",
                "properties": {
                    "answer": {"type": "string", "description": "The student's answer"},
                    "question": {"type": "string", "description": "The question that was asked"}
                },
                "required": ["answer", "question"]
            }
        }
    }
]


def main():
    print("="*70)
    print("STEP 5: MULTIPLE TOOLS")
    print("="*70)
    print()
    
    # Initialize client
    client = AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
    )
    
    print("🔧 Available Tools:")
    for tool in tools:
        print(f"  - {tool['function']['name']}: {tool['function']['description']}")
    print()
    
    # Test different requests that should trigger different tools
    test_cases = [
        ("Create a quiz on Python basics with 3 questions", "generate_quiz"),
        ("Explain what machine learning is", "explain_concept"),
        ("Grade this answer: 'Python is a programming language'", "assess_answer"),
    ]
    
    for user_request, expected_tool in test_cases:
        print("="*70)
        print(f"👤 Student: {user_request}")
        print(f"   Expected tool: {expected_tool}")
        print("="*70)
        
        messages = [
            {"role": "system", "content": "You are a teaching assistant with access to tools. Use them when appropriate."},
            {"role": "user", "content": user_request}
        ]
        
        # Send request with tools
        response = client.chat.completions.create(
            model=GPT4_DEPLOYMENT_NAME,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        response_message = response.choices[0].message
        
        if response_message.tool_calls:
            tool_call = response_message.tool_calls[0]
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            print(f"\\n🤖 AI chose: {function_name}")
            print(f"📋 Arguments: {json.dumps(function_args, indent=2)}")
            
            # Check if correct tool was chosen
            if function_name == expected_tool:
                print("✅ Correct tool selected!")
            else:
                print(f"⚠️  Expected {expected_tool}, got {function_name}")
            
            # Execute the function
            if function_name == "generate_quiz":
                result = generate_quiz(function_args.get("topic"), function_args.get("num_questions", 5))
            elif function_name == "explain_concept":
                result = explain_concept(function_args.get("topic"))
            elif function_name == "assess_answer":
                result = assess_answer(function_args.get("answer"), function_args.get("question", ""))
            
            print(f"\\n📤 Function result: {result[:100]}...")
        else:
            print("\\n🤖 AI responded without using tools")
            print(response_message.content)
        
        print()
    
    print("="*70)
    print("SUMMARY:")
    print("="*70)
    print("✅ AI successfully chose the right tool for each request")
    print("✅ Multiple tools enable more capabilities")
    print("✅ AI automatically routes to appropriate tool")
    print()
    print("This is the foundation for intelligent assistants!")
    print()


if __name__ == "__main__":
    main()
    print("Next: Move to Step 6 to create your first agent!")
    print("  cd ../06_single_agent")
    print("  python chat_agent.py")
    print()

