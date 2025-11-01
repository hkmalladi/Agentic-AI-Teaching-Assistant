"""
Step 3: Streaming Output - Real-time Responses

This script demonstrates streaming responses from GPT-4.
Watch the text appear word-by-word in real-time!
"""

import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    GPT4_DEPLOYMENT_NAME
)


def main():
    print("="*70)
    print("STEP 3: STREAMING OUTPUT")
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
    
    # Create messages
    messages = [
        {"role": "system", "content": "You are a helpful teaching assistant."},
        {"role": "user", "content": "Explain what machine learning is in about 150 words."}
    ]
    
    print("📝 Question: Explain what machine learning is")
    print()
    print("🚀 Sending request with streaming enabled...")
    print()
    print("="*70)
    print("STREAMING RESPONSE:")
    print("="*70)
    print()
    
    # Record start time
    start_time = time.time()
    first_chunk_time = None
    
    # Make streaming request
    stream = client.chat.completions.create(
        model=GPT4_DEPLOYMENT_NAME,
        messages=messages,
        temperature=0.7,
        max_tokens=500,
        stream=True  # ⭐ This enables streaming!
    )
    
    # Process chunks as they arrive
    full_response = ""
    for chunk in stream:
        # Check if chunk has content
        if chunk.choices[0].delta.content:
            # Record time of first chunk
            if first_chunk_time is None:
                first_chunk_time = time.time()
            
            # Get the text chunk
            text_chunk = chunk.choices[0].delta.content
            full_response += text_chunk
            
            # Print immediately (this is the key to streaming!)
            print(text_chunk, end="", flush=True)
    
    # Record end time
    end_time = time.time()
    
    print("\n")
    print("="*70)
    print("METRICS:")
    print("="*70)
    print(f"⏱️  Time to first chunk: {first_chunk_time - start_time:.2f} seconds")
    print(f"⏱️  Total time: {end_time - start_time:.2f} seconds")
    print(f"📊 Response length: {len(full_response)} characters")
    print()
    
    print("="*70)
    print("SUMMARY:")
    print("="*70)
    print("✅ Response streamed in real-time")
    print("✅ Text appeared immediately")
    print("✅ Much better user experience!")
    print()


if __name__ == "__main__":
    main()
    print("Try running comparison.py to see streaming vs non-streaming!")
    print("  python comparison.py")
    print()

