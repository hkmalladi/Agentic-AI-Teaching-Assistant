"""
Step 7: Multiple Agents - Chat Agent

One of three specialized agents. This one handles conversations.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import AzureOpenAI
from config import *


class ChatAgent:
    """
    Chat Agent - Handles conversational interactions
    
    Purpose: General conversation and questions
    """
    
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
        
        self.system_prompt = "You are a friendly teaching assistant who helps students learn through conversation."
        self.messages = [{"role": "system", "content": self.system_prompt}]
    
    def chat(self, user_message):
        """Handle a chat message"""
        self.messages.append({"role": "user", "content": user_message})
        
        response = self.client.chat.completions.create(
            model=GPT4_DEPLOYMENT_NAME,
            messages=self.messages,
            temperature=0.7
        )
        
        response_text = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response_text})
        
        return response_text


if __name__ == "__main__":
    print("Testing ChatAgent...")
    agent = ChatAgent()
    
    response = agent.chat("What is Python?")
    print(f"Response: {response}")

