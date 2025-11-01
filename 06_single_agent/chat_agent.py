"""
Step 6: Single Agent - Creating a Specialized Component

This demonstrates creating a ChatAgent - a reusable, specialized component.
This is the foundation for building modular AI systems!
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    GPT4_DEPLOYMENT_NAME
)


class ChatAgent:
    """
    Chat Agent - Handles conversational interactions
    
    This is an AGENT - a specialized, reusable component with:
    - Specific purpose (chat/conversation)
    - Own system prompt (defines behavior)
    - Own state (conversation history)
    - Independent operation
    
    Think of it as a specialized AI worker!
    """
    
    def __init__(self):
        """Initialize the chat agent"""
        print("🤖 Initializing ChatAgent...")
        
        # Create Azure OpenAI client
        self.client = AzureOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
        )
        
        # Agent's system prompt defines its behavior
        # This makes the agent friendly and helpful
        self.system_prompt = """You are a friendly teaching assistant who helps students learn.
        You explain concepts clearly, provide examples, and encourage questions."""
        
        # Agent maintains its own conversation history
        self.messages = [
            {"role": "system", "content": self.system_prompt}
        ]
        
        print("✅ ChatAgent ready!")
    
    def chat(self, user_message):
        """
        Process a chat message
        
        This is the main interface to the agent.
        Users just call .chat() and get a response!
        
        Args:
            user_message: Message from the user
        
        Returns:
            AI's response
        """
        # Add user message to conversation history
        self.messages.append({
            "role": "user",
            "content": user_message
        })
        
        # Get response from GPT-4
        response = self.client.chat.completions.create(
            model=GPT4_DEPLOYMENT_NAME,
            messages=self.messages,
            temperature=0.7
        )
        
        # Extract response text
        response_text = response.choices[0].message.content
        
        # Add response to conversation history
        # This maintains context for future messages
        self.messages.append({
            "role": "assistant",
            "content": response_text
        })
        
        return response_text


def main():
    """
    Demonstrate the ChatAgent
    """
    print("="*70)
    print("STEP 6: SINGLE AGENT")
    print("="*70)
    print()
    
    # ========================================================================
    # CREATE THE AGENT
    # ========================================================================
    # This is much cleaner than managing everything manually!
    agent = ChatAgent()
    print()
    
    # ========================================================================
    # USE THE AGENT
    # ========================================================================
    print("="*70)
    print("TESTING THE AGENT")
    print("="*70)
    print()
    
    # Test with multiple questions
    questions = [
        "What is Python?",
        "Can you give me an example?",
        "What can I build with it?"
    ]
    
    for question in questions:
        print(f"👤 Student: {question}")
        
        # Simple interface - just call .chat()!
        response = agent.chat(question)
        
        print(f"🤖 Agent: {response}")
        print()
    
    # ========================================================================
    # SHOW AGENT STATE
    # ========================================================================
    print("="*70)
    print("AGENT STATE:")
    print("="*70)
    print(f"Conversation length: {len(agent.messages)} messages")
    print(f"System prompt: {agent.system_prompt[:50]}...")
    print()
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    print("="*70)
    print("SUMMARY:")
    print("="*70)
    print("✅ Created a reusable ChatAgent class")
    print("✅ Agent maintains its own state")
    print("✅ Agent has specific behavior (friendly teacher)")
    print("✅ Agent provides clean interface (.chat())")
    print("✅ Agent can be used independently")
    print()
    print("This is the foundation for modular AI systems!")
    print()
    
    # ========================================================================
    # BENEFITS OF AGENTS
    # ========================================================================
    print("="*70)
    print("WHY USE AGENTS?")
    print("="*70)
    print()
    print("1. **Encapsulation:**")
    print("   All AI logic is contained in the class")
    print()
    print("2. **Reusability:**")
    print("   Can create multiple instances:")
    print("   agent1 = ChatAgent()")
    print("   agent2 = ChatAgent()")
    print()
    print("3. **Maintainability:**")
    print("   Easy to modify and test")
    print()
    print("4. **Scalability:**")
    print("   Foundation for multi-agent systems")
    print()


if __name__ == "__main__":
    main()
    print("="*70)
    print("NEXT STEP:")
    print("="*70)
    print("Now that you understand agents, create multiple specialized agents!")
    print()
    print("Move to Step 7:")
    print("  cd ../07_multiple_agents")
    print("  python chat_agent.py")
    print()

