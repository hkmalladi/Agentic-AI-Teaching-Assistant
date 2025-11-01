"""
Step 9: Complete UI - FastAPI Backend

This is the backend API that replaces Streamlit.
It exposes REST endpoints for the React frontend to interact with the orchestrator.

Run with: uvicorn api:app --reload
"""

import sys
import os
from typing import List, Optional
from datetime import datetime

# Add path for config import (go up 3 levels to reach project root)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import orchestrator from same directory
from orchestrator import Orchestrator


# ============================================================================
# Pydantic Models for Request/Response
# ============================================================================

class Message(BaseModel):
    """Message model for chat history"""
    role: str  # "user" or "assistant"
    content: str
    agent: Optional[str] = None
    timestamp: str


class ChatRequest(BaseModel):
    """Request model for chat endpoint"""
    message: str
    conversation_history: List[Message] = []


class ChatResponse(BaseModel):
    """Response model for chat endpoint"""
    response: str
    agent: str
    timestamp: str


class HealthResponse(BaseModel):
    """Response model for health check"""
    status: str
    message: str


# ============================================================================
# FastAPI Application
# ============================================================================

app = FastAPI(
    title="AI Teaching Assistant API",
    description="Backend API for the AI Teaching Assistant built from scratch",
    version="1.0.0"
)

# Configure CORS to allow React frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize orchestrator (singleton pattern)
orchestrator = Orchestrator()


# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint - health check"""
    return {
        "status": "healthy",
        "message": "AI Teaching Assistant API is running!"
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "All systems operational"
    }


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint
    
    Receives a user message and returns AI response with agent information
    """
    try:
        # Get the user's message
        user_message = request.message
        
        if not user_message or not user_message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Route the request to appropriate agent
        agent_name = orchestrator.route_request(user_message)
        
        # Get response from the appropriate agent
        if agent_name == "quiz":
            response = orchestrator.quiz_agent.generate_quiz(user_message, 3)
        elif agent_name == "explanation":
            response = orchestrator.explanation_agent.explain(user_message)
        else:  # Default to chat
            response = orchestrator.chat_agent.chat(user_message)
        
        # Return response with metadata
        return {
            "response": response,
            "agent": agent_name,
            "timestamp": datetime.now().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@app.post("/api/route", response_model=dict)
async def route_message(request: ChatRequest):
    """
    Route endpoint - determines which agent should handle the message
    
    Useful for showing users which agent will be used before sending
    """
    try:
        user_message = request.message
        
        if not user_message or not user_message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Determine which agent to use
        agent_name = orchestrator.route_request(user_message)
        
        return {
            "agent": agent_name,
            "timestamp": datetime.now().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error routing request: {str(e)}")


@app.get("/api/agents", response_model=dict)
async def get_agents():
    """
    Get information about available agents
    """
    return {
        "agents": [
            {
                "name": "chat",
                "description": "General conversation and questions",
                "icon": "💬",
                "color": "blue"
            },
            {
                "name": "quiz",
                "description": "Generate quizzes and practice problems",
                "icon": "📝",
                "color": "green"
            },
            {
                "name": "explanation",
                "description": "Detailed explanations of concepts",
                "icon": "🧠",
                "color": "purple"
            }
        ]
    }


# ============================================================================
# Startup Event
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    print("=" * 70)
    print("🚀 AI Teaching Assistant API Starting...")
    print("=" * 70)
    print("✅ Orchestrator initialized")
    print("✅ All agents ready")
    print("✅ API endpoints available")
    print()
    print("📡 API Documentation: http://localhost:8000/docs")
    print("🎓 Ready to assist students!")
    print("=" * 70)


# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print("Starting AI Teaching Assistant API...")
    print("Access the API at: http://localhost:8000")
    print("Access the docs at: http://localhost:8000/docs")
    
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

