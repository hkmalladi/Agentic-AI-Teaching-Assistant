"""
Step 3: Streaming vs Non-Streaming Comparison

This script compares streaming and non-streaming side-by-side.
See the difference in user experience!
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


def non_streaming_request(client, messages):
    """Make a non-streaming request"""
    print("⏳ Waiting for complete response...")
    
    start_time = time.time()
    
    response = client.chat.completions.create(
        model=GPT4_DEPLOYMENT_NAME,
        messages=messages,
        temperature=0.7,
        max_tokens=500,
        stream=False  # Non-streaming
    )
    
    end_time = time.time()
    
    text = response.choices[0].message.content
    print(text)
    
    return end_time - start_time, len(text)


def streaming_request(client, messages):
    """Make a streaming request"""
    start_time = time.time()
    first_chunk_time = None
    
    stream = client.chat.completions.create(
        model=GPT4_DEPLOYMENT_NAME,
        messages=messages,
        temperature=0.7,
        max_tokens=500,
        stream=True  # Streaming!
    )
    
    full_response = ""
    for chunk in stream:
        # Check if choices list is not empty and has content
        if chunk.choices and chunk.choices[0].delta.content:
            if first_chunk_time is None:
                first_chunk_time = time.time()

            text_chunk = chunk.choices[0].delta.content
            full_response += text_chunk
            print(text_chunk, end="", flush=True)
    
    print()  # New line after streaming
    end_time = time.time()
    
    return {
        'total_time': end_time - start_time,
        'first_chunk_time': first_chunk_time - start_time,
        'length': len(full_response)
    }


def main():
    print("="*70)
    print("STREAMING VS NON-STREAMING COMPARISON")
    print("="*70)
    print()
    
    # Initialize client
    client = AzureOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
    )
    
    # Same question for both
    messages = [
        {"role": "system", "content": "You are a helpful teaching assistant."},
        {"role": "user", "content": "Explain photosynthesis in about 150 words."}
    ]
    
    # ========================================================================
    # TEST 1: NON-STREAMING
    # ========================================================================
    print("TEST 1: NON-STREAMING")
    print("="*70)
    print()
    
    non_stream_time, non_stream_length = non_streaming_request(client, messages)
    
    print()
    print(f"⏱️  Total time: {non_stream_time:.2f} seconds")
    print(f"📊 Length: {non_stream_length} characters")
    print()
    
    print("💭 Notice: You waited, then saw the full response at once")
    print()
    
    input("Press Enter to see streaming version...")
    print()
    
    # ========================================================================
    # TEST 2: STREAMING
    # ========================================================================
    print("TEST 2: STREAMING")
    print("="*70)
    print()
    
    stream_metrics = streaming_request(client, messages)
    
    print()
    print(f"⏱️  Time to first chunk: {stream_metrics['first_chunk_time']:.2f} seconds")
    print(f"⏱️  Total time: {stream_metrics['total_time']:.2f} seconds")
    print(f"📊 Length: {stream_metrics['length']} characters")
    print()
    
    print("💭 Notice: Text appeared immediately and gradually")
    print()
    
    # ========================================================================
    # COMPARISON
    # ========================================================================
    print("="*70)
    print("COMPARISON:")
    print("="*70)
    print()
    print(f"Non-Streaming:")
    print(f"  ⏱️  Total time: {non_stream_time:.2f}s")
    print(f"  👁️  User saw nothing until: {non_stream_time:.2f}s")
    print()
    print(f"Streaming:")
    print(f"  ⏱️  Total time: {stream_metrics['total_time']:.2f}s")
    print(f"  👁️  User saw first text at: {stream_metrics['first_chunk_time']:.2f}s")
    print()
    
    improvement = non_stream_time - stream_metrics['first_chunk_time']
    print(f"🚀 Streaming felt {improvement:.2f} seconds faster!")
    print()
    
    print("="*70)
    print("KEY INSIGHT:")
    print("="*70)
    print("Total time is similar, but streaming FEELS much faster")
    print("because users see progress immediately!")
    print()


if __name__ == "__main__":
    main()

