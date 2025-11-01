"""
Step 7: Multiple Agents - Explanation Agent

One of three specialized agents. This one explains concepts.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import AzureOpenAI
from config import *


class ExplanationAgent:
    """
    Explanation Agent - Explains concepts clearly
    
    Purpose: Provide detailed explanations with examples
    """
    
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
        
        self.system_prompt = """You are an explanation specialist.
        Explain concepts clearly with:
        1. Simple definition
        2. Key points
        3. Real-world example
        4. Common misconceptions"""
    
    def explain(self, topic):
        """Explain a concept"""
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"Explain {topic}"}
        ]
        
        response = self.client.chat.completions.create(
            model=GPT4_DEPLOYMENT_NAME,
            messages=messages,
            temperature=0.7
        )
        
        return response.choices[0].message.content


if __name__ == "__main__":
    print("Testing ExplanationAgent...")
    agent = ExplanationAgent()
    
    explanation = agent.explain("machine learning")
    print(f"Explanation:\\n{explanation}")

