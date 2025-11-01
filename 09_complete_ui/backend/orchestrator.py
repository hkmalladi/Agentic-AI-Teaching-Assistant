"""
Step 9: Complete UI - Orchestrator

This is a copy of the Orchestrator for Step 9 to keep this folder self-contained.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the agents from THIS folder (self-contained)
from chat_agent import ChatAgent
from quiz_agent import QuizAgent
from explanation_agent import ExplanationAgent

from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    GPT4_DEPLOYMENT_NAME
)


class Orchestrator:
    """
    Orchestrator - Routes requests to appropriate agents
    
    This is the coordinator that:
    1. Receives all user requests
    2. Determines which agent should handle it
    3. Routes to the appropriate agent
    4. Returns the result
    
    Think of it as a traffic controller for AI agents!
    """
    
    def __init__(self):
        """Initialize the orchestrator and all agents"""
        # Create all specialized agents
        self.chat_agent = ChatAgent()
        self.quiz_agent = QuizAgent()
        self.explanation_agent = ExplanationAgent()
        
        # Client for routing decisions
        self.client = AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
    
    def route_request(self, user_message):
        """
        Determine which agent should handle the request
        
        Args:
            user_message: The user's request
        
        Returns:
            Agent name to use
        """
        # Use AI to determine routing
        routing_prompt = f"""Given this user request, which agent should handle it?

User request: "{user_message}"

Available agents:
- chat: General conversation and questions
- quiz: Generate quizzes and practice problems
- explanation: Detailed explanations of concepts

Respond with ONLY the agent name (chat, quiz, or explanation)."""

        response = self.client.chat.completions.create(
            model=GPT4_DEPLOYMENT_NAME,
            messages=[{"role": "user", "content": routing_prompt}],
            temperature=0.3,
            max_tokens=10
        )
        
        agent_name = response.choices[0].message.content.strip().lower()
        return agent_name
    
    def process_request(self, user_message):
        """
        Process a user request by routing to the appropriate agent
        
        Args:
            user_message: The user's request
        
        Returns:
            Tuple of (response, agent_name)
        """
        # Determine which agent to use
        agent_name = self.route_request(user_message)
        
        # Route to the appropriate agent
        if agent_name == "quiz":
            # Extract topic from message (simplified)
            response = self.quiz_agent.generate_quiz(user_message, 3)
        elif agent_name == "explanation":
            response = self.explanation_agent.explain(user_message)
        else:  # Default to chat
            response = self.chat_agent.chat(user_message)
        
        return response, agent_name

