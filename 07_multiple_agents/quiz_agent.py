"""
Step 7: Multiple Agents - Quiz Agent

One of three specialized agents. This one generates quizzes.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import AzureOpenAI
from config import *


class QuizAgent:
    """
    Quiz Agent - Generates quizzes and practice problems
    
    Purpose: Create quizzes on any topic
    """
    
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
        
        self.system_prompt = """You are a quiz generation specialist. 
        Create clear, educational quizzes with multiple choice questions.
        Format: Question, 4 options (A-D), and indicate the correct answer."""
    
    def generate_quiz(self, topic, num_questions=5):
        """Generate a quiz on a topic"""
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"Create a {num_questions}-question quiz on {topic}"}
        ]
        
        response = self.client.chat.completions.create(
            model=GPT4_DEPLOYMENT_NAME,
            messages=messages,
            temperature=0.7
        )
        
        return response.choices[0].message.content


if __name__ == "__main__":
    print("Testing QuizAgent...")
    agent = QuizAgent()
    
    quiz = agent.generate_quiz("Python basics", 3)
    print(f"Quiz:\\n{quiz}")

