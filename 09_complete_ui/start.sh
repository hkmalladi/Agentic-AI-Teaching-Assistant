#!/bin/bash

# AI Teaching Assistant - Quick Start Script
# This script starts both backend and frontend in separate terminal windows

echo "🚀 Starting AI Teaching Assistant..."
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -d "backend" ] || [ ! -d "frontend" ]; then
    echo -e "${RED}❌ Error: Please run this script from the 09_complete_ui directory${NC}"
    exit 1
fi

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "📋 Checking prerequisites..."

if ! command_exists python3; then
    echo -e "${RED}❌ Python 3 is not installed${NC}"
    exit 1
fi

if ! command_exists node; then
    echo -e "${RED}❌ Node.js is not installed${NC}"
    exit 1
fi

if ! command_exists npm; then
    echo -e "${RED}❌ npm is not installed${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All prerequisites met${NC}"
echo ""

# Start backend
echo -e "${BLUE}🐍 Starting Backend (FastAPI)...${NC}"

# Check if running on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS - use osascript to open new Terminal window
    osascript <<EOF
tell application "Terminal"
    do script "cd '$PWD/backend' && echo '🐍 Backend Terminal' && echo 'Installing dependencies...' && pip3 install -r requirements.txt && echo '' && echo '🚀 Starting FastAPI server...' && uvicorn api:app --reload"
    activate
end tell
EOF
    echo -e "${GREEN}✅ Backend terminal opened${NC}"
else
    # Linux - try different terminal emulators
    if command_exists gnome-terminal; then
        gnome-terminal -- bash -c "cd '$PWD/backend' && echo '🐍 Backend Terminal' && echo 'Installing dependencies...' && pip3 install -r requirements.txt && echo '' && echo '🚀 Starting FastAPI server...' && uvicorn api:app --reload; exec bash"
    elif command_exists xterm; then
        xterm -e "cd '$PWD/backend' && echo '🐍 Backend Terminal' && echo 'Installing dependencies...' && pip3 install -r requirements.txt && echo '' && echo '🚀 Starting FastAPI server...' && uvicorn api:app --reload; exec bash" &
    else
        echo -e "${RED}❌ No suitable terminal emulator found${NC}"
        echo "Please manually run: cd backend && uvicorn api:app --reload"
    fi
    echo -e "${GREEN}✅ Backend terminal opened${NC}"
fi

# Wait a bit for backend to start
sleep 2

# Start frontend
echo -e "${BLUE}⚛️  Starting Frontend (React)...${NC}"

# Check if running on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS - use osascript to open new Terminal window
    osascript <<EOF
tell application "Terminal"
    do script "cd '$PWD/frontend' && echo '⚛️  Frontend Terminal' && echo 'Installing dependencies...' && npm install && echo '' && echo '🚀 Starting React dev server...' && npm run dev"
    activate
end tell
EOF
    echo -e "${GREEN}✅ Frontend terminal opened${NC}"
else
    # Linux - try different terminal emulators
    if command_exists gnome-terminal; then
        gnome-terminal -- bash -c "cd '$PWD/frontend' && echo '⚛️  Frontend Terminal' && echo 'Installing dependencies...' && npm install && echo '' && echo '🚀 Starting React dev server...' && npm run dev; exec bash"
    elif command_exists xterm; then
        xterm -e "cd '$PWD/frontend' && echo '⚛️  Frontend Terminal' && echo 'Installing dependencies...' && npm install && echo '' && echo '🚀 Starting React dev server...' && npm run dev; exec bash" &
    else
        echo -e "${RED}❌ No suitable terminal emulator found${NC}"
        echo "Please manually run: cd frontend && npm run dev"
    fi
    echo -e "${GREEN}✅ Frontend terminal opened${NC}"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}🎉 AI Teaching Assistant is starting!${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📡 Backend will be available at: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "🌐 Frontend will be available at: http://localhost:3000"
echo ""
echo "⏳ Please wait for both servers to start..."
echo "   (This may take a minute on first run)"
echo ""
echo "💡 Tip: Check the new terminal windows for startup progress"
echo ""
echo "To stop the servers:"
echo "  - Press Ctrl+C in each terminal window"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

