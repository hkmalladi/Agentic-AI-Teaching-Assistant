"""
Step 1: Basic Prompt - The Simplest AI Interaction

This script demonstrates the most basic way to interact with GPT-4:
1. Create a system prompt (defines AI behavior)
2. Create a user prompt (the actual question)
3. Send to GPT-4 and get a response

This is the foundation for everything else!
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


def main():
    """
    Main function - demonstrates a basic prompt to GPT-4
    """
    
    print("="*70)
    print("STEP 1: BASIC PROMPT")
    print("="*70)
    print()
    
    # ========================================================================
    # STEP 1: Initialize the Azure OpenAI Client
    # ========================================================================
    print("📡 Initializing Azure OpenAI client...")
    
    try:
        client = AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
        print("✅ Client initialized successfully!")
        print()
    except Exception as e:
        print(f"❌ Error initializing client: {e}")
        return
    
    # ========================================================================
    # STEP 2: Create the Messages
    # ========================================================================
    print("📝 Creating messages...")
    print()
    
    # The SYSTEM prompt defines how the AI should behave
    system_prompt = "You are a helpful teaching assistant who explains concepts clearly and simply."
    
    # The USER prompt is the actual question
    user_prompt = "What is photosynthesis? Explain it in simple terms."
    
    # Azure OpenAI expects messages in this format
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user", 
            "content": user_prompt
        }
    ]
    
    # Show what we're sending
    print("System Prompt:")
    print(f"  '{system_prompt}'")
    print()
    print("User Prompt:")
    print(f"  '{user_prompt}'")
    print()
    
    # ========================================================================
    # STEP 3: Send the Request to GPT-4
    # ========================================================================
    print("🚀 Sending request to GPT-4...")
    print()
    
    try:
        # Record start time to measure latency
        start_time = time.time()
        
        # Make the API call
        response = client.chat.completions.create(
            model=GPT4_DEPLOYMENT_NAME,      # Which model to use
            messages=messages,                # The conversation
            temperature=0.7,                  # Creativity (0=focused, 1=creative)
            max_tokens=500                    # Maximum length of response
        )
        
        # Record end time
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print(f"✅ Response received in {elapsed_time:.2f} seconds!")
        print()
        
    except Exception as e:
        print(f"❌ Error getting response: {e}")
        return
    
    # ========================================================================
    # STEP 4: Display the Response
    # ========================================================================
    print("="*70)
    print("RESPONSE FROM GPT-4:")
    print("="*70)
    print()
    
    # Extract the response text
    response_text = response.choices[0].message.content
    print(response_text)
    print()
    
    # ========================================================================
    # BONUS: Show Response Metadata
    # ========================================================================
    print("="*70)
    print("METADATA:")
    print("="*70)
    print(f"Model used: {response.model}")
    print(f"Tokens used: {response.usage.total_tokens}")
    print(f"  - Prompt tokens: {response.usage.prompt_tokens}")
    print(f"  - Completion tokens: {response.usage.completion_tokens}")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print()
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    print("="*70)
    print("SUMMARY:")
    print("="*70)
    print("✅ We sent a system prompt (defines AI behavior)")
    print("✅ We sent a user prompt (the actual question)")
    print("✅ We got a response from GPT-4")
    print("✅ The AI followed the system prompt's instructions")
    print()
    print("This is the foundation for all AI interactions!")
    print()


if __name__ == "__main__":
    main()
    
    # ========================================================================
    # NEXT STEPS
    # ========================================================================
    print("="*70)
    print("NEXT STEP:")
    print("="*70)
    print("Now that you understand basic prompts, try:")
    print()
    print("1. Modify the system prompt to change AI behavior")
    print("2. Try different user questions")
    print("3. Experiment with temperature values")
    print()
    print("When ready, move to Step 2: Conversation History")
    print("  cd ../02_conversation_history")
    print("  python conversation.py")
    print()

