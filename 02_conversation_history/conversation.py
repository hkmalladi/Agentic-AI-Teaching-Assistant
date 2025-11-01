"""
Step 2: Conversation History - Maintaining Context

This script demonstrates how to maintain context across multiple messages:
1. Send a question and get a response
2. Add the response to conversation history
3. Ask a follow-up question that refers to previous context
4. Get a contextual response

This is essential for natural conversations!
"""

import sys
import os
import time

# Add parent directory to path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    GPT4_DEPLOYMENT_NAME
)


def get_response(client, messages):
    """
    Helper function to get a response from GPT-4
    
    Args:
        client: Azure OpenAI client
        messages: List of conversation messages
    
    Returns:
        Response text from GPT-4
    """
    response = client.chat.completions.create(
        model=GPT4_DEPLOYMENT_NAME,
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content


def main():
    """
    Main function - demonstrates conversation with context
    """
    
    print("="*70)
    print("STEP 2: CONVERSATION HISTORY")
    print("="*70)
    print()
    
    # ========================================================================
    # STEP 1: Initialize Client
    # ========================================================================
    print("📡 Initializing Azure OpenAI client...")
    
    try:
        client = AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
        print("✅ Client initialized!")
        print()
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # ========================================================================
    # STEP 2: Start the Conversation
    # ========================================================================
    print("💬 Starting conversation...")
    print()
    
    # Initialize messages with system prompt
    # This defines the AI's role throughout the conversation
    messages = [
        {
            "role": "system",
            "content": "You are a helpful teaching assistant who explains concepts clearly."
        }
    ]
    
    print("System prompt set: Teaching assistant mode")
    print()
    
    # ========================================================================
    # TURN 1: First Question
    # ========================================================================
    print("="*70)
    print("TURN 1: First Question")
    print("="*70)
    print()
    
    # Student asks the first question
    first_question = "What is machine learning?"
    
    print(f"👤 Student: {first_question}")
    print()
    
    # Add user message to conversation
    messages.append({
        "role": "user",
        "content": first_question
    })
    
    # Get response
    print("🤖 AI is thinking...")
    response_1 = get_response(client, messages)
    
    print(f"🤖 AI: {response_1}")
    print()
    
    # ⭐ IMPORTANT: Add the AI's response to the conversation history
    # This is how we maintain context!
    messages.append({
        "role": "assistant",
        "content": response_1
    })
    
    print("✅ Response added to conversation history")
    print(f"   Current history length: {len(messages)} messages")
    print()
    
    # ========================================================================
    # TURN 2: Follow-up Question (Uses Context!)
    # ========================================================================
    print("="*70)
    print("TURN 2: Follow-up Question")
    print("="*70)
    print()
    
    # Student asks a follow-up question
    # Notice: We don't say "example of machine learning"
    # The AI will know from context!
    follow_up_question = "Can you give me a simple example?"
    
    print(f"👤 Student: {follow_up_question}")
    print()
    print("   ⭐ Notice: We didn't say 'example of machine learning'")
    print("      The AI knows from context!")
    print()
    
    # Add user message to conversation
    messages.append({
        "role": "user",
        "content": follow_up_question
    })
    
    print('Messages: ', messages)

    # Get response
    print("🤖 AI is thinking...")
    response_2 = get_response(client, messages)
    
    print(f"🤖 AI: {response_2}")
    print()
    
    # Add response to history
    messages.append({
        "role": "assistant",
        "content": response_2
    })
    
    print("✅ Response added to conversation history")
    print(f"   Current history length: {len(messages)} messages")
    print()
    
    # ========================================================================
    # TURN 3: Another Follow-up
    # ========================================================================
    print("="*70)
    print("TURN 3: Another Follow-up")
    print("="*70)
    print()
    
    # Another follow-up that uses context
    third_question = "What are some real-world applications?"
    
    print(f"👤 Student: {third_question}")
    print()
    print("   ⭐ Again, we don't specify 'applications of machine learning'")
    print("      The AI maintains context!")
    print()
    
    # Add to conversation
    messages.append({
        "role": "user",
        "content": third_question
    })
    
    # Get response
    print("🤖 AI is thinking...")
    response_3 = get_response(client, messages)
    
    print(f"🤖 AI: {response_3}")
    print()
    
    # ========================================================================
    # SHOW THE FULL CONVERSATION HISTORY
    # ========================================================================
    print("="*70)
    print("FULL CONVERSATION HISTORY:")
    print("="*70)
    print()
    
    for i, msg in enumerate(messages, 1):
        role = msg["role"].upper()
        content = msg["content"]
        
        # Truncate long messages for display
        if len(content) > 100:
            content = content[:100] + "..."
        
        print(f"{i}. [{role}] {content}")
    
    print()
    print(f"Total messages in history: {len(messages)}")
    print()
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    print("="*70)
    print("SUMMARY:")
    print("="*70)
    print("✅ We maintained context across 3 turns")
    print("✅ Each follow-up question used previous context")
    print("✅ The AI understood references without explicit mentions")
    print("✅ We built this by adding each message to history")
    print()
    print("This is how chatbots maintain natural conversations!")
    print()


if __name__ == "__main__":
    main()
    
    # ========================================================================
    # NEXT STEPS
    # ========================================================================
    print("="*70)
    print("NEXT STEP:")
    print("="*70)
    print("Now that you understand conversation history, try:")
    print()
    print("1. Add more turns to the conversation")
    print("2. Try removing history and see what breaks")
    print("3. Experiment with changing topics mid-conversation")
    print()
    print("When ready, move to Step 3: Streaming")
    print("  cd ../03_streaming")
    print("  python streaming.py")
    print()

