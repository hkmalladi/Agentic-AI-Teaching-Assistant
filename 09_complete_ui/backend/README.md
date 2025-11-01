# Backend - FastAPI Server

This folder contains all the backend Python code for the AI Teaching Assistant.

## 📁 Structure

```
backend/
├── api.py                    # FastAPI application with REST endpoints
├── orchestrator.py           # Routes requests to appropriate agents
├── chat_agent.py            # Handles general chat conversations
├── quiz_agent.py            # Generates quizzes and practice problems
├── explanation_agent.py     # Provides detailed explanations
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Azure OpenAI

Make sure the `config.py` file in the project root (2 levels up) has your Azure OpenAI credentials:

```python
# ../../config.py
AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
AZURE_OPENAI_API_KEY = "your-api-key-here"
AZURE_OPENAI_API_VERSION = "2024-02-15-preview"
GPT4_DEPLOYMENT_NAME = "gpt-4"
```

### 3. Run the Server

```bash
uvicorn api:app --reload
```

The server will start at: **http://localhost:8000**

## 📡 API Endpoints

### `POST /api/chat`
Send a message and get a response from the appropriate agent.

**Request:**
```json
{
  "message": "What is Python?",
  "conversation_history": []
}
```

**Response:**
```json
{
  "response": "Python is a high-level programming language...",
  "agent": "chat",
  "timestamp": "2024-10-31T12:00:00"
}
```

### `GET /api/agents`
Get information about all available agents.

**Response:**
```json
{
  "agents": [
    {
      "name": "chat",
      "description": "General conversation and questions",
      "icon": "💬"
    },
    {
      "name": "quiz",
      "description": "Generate quizzes and practice problems",
      "icon": "📝"
    },
    {
      "name": "explanation",
      "description": "Detailed explanations of concepts",
      "icon": "🧠"
    }
  ]
}
```

### `GET /health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-10-31T12:00:00"
}
```

### `GET /docs`
Interactive API documentation (Swagger UI).

Visit: **http://localhost:8000/docs**

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│         FastAPI (api.py)            │
│  • REST endpoints                   │
│  • CORS middleware                  │
│  • Request/Response validation      │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Orchestrator                   │
│  • Routes requests to agents        │
│  • Determines intent                │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┐
    ↓          ↓           ↓
┌────────┐ ┌────────┐ ┌────────┐
│ Chat   │ │ Quiz   │ │Explain │
│ Agent  │ │ Agent  │ │ Agent  │
└────────┘ └────────┘ └────────┘
    │          │           │
    └──────────┼───────────┘
               ↓
    ┌─────────────────────┐
    │  Azure OpenAI GPT-4 │
    └─────────────────────┘
```

## 🔧 Development

### Run with Auto-Reload

```bash
uvicorn api:app --reload
```

Changes to Python files will automatically reload the server.

### Run on Different Port

```bash
uvicorn api:app --reload --port 8001
```

### Run with Custom Host

```bash
uvicorn api:app --reload --host 0.0.0.0
```

This allows access from other devices on your network.

## 🧪 Testing

### Test with curl

```bash
# Health check
curl http://localhost:8000/health

# Get agents
curl http://localhost:8000/api/agents

# Send a message
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Python?"}'
```

### Test with Python

```python
import requests

# Send a message
response = requests.post(
    "http://localhost:8000/api/chat",
    json={"message": "What is Python?"}
)
print(response.json())
```

## 📦 Dependencies

- **fastapi** - Modern web framework
- **uvicorn** - ASGI server
- **pydantic** - Data validation
- **openai** - Azure OpenAI SDK
- **python-dotenv** - Environment variables
- **python-multipart** - File upload support

## 🐛 Troubleshooting

### Port Already in Use

```bash
# macOS/Linux
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Module Not Found

Make sure you're in the backend directory and have installed dependencies:

```bash
cd backend
pip install -r requirements.txt
```

### Azure OpenAI Errors

- Check your `config.py` credentials
- Verify your Azure OpenAI resource is active
- Ensure deployment name matches your setup

## 🚀 Production Deployment

### Using Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t ai-teaching-assistant-backend .
docker run -p 8000:8000 ai-teaching-assistant-backend
```

### Using Cloud Platforms

- **Azure**: Azure App Service or Container Instances
- **AWS**: Elastic Beanstalk or ECS
- **GCP**: Cloud Run or App Engine
- **Heroku**: `heroku create` and `git push heroku main`

## 📝 Notes

- All agent files are self-contained in this folder
- The orchestrator coordinates between agents
- CORS is configured to allow requests from the React frontend
- API documentation is auto-generated at `/docs`

