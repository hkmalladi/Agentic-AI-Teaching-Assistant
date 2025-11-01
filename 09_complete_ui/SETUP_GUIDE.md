# 🚀 Setup Guide - AI Teaching Assistant

Complete step-by-step guide to run the React + FastAPI application.

---

## 📋 Prerequisites

Before you start, make sure you have:

- ✅ **Python 3.8+** installed ([Download](https://www.python.org/downloads/))
- ✅ **Node.js 18+** and npm installed ([Download](https://nodejs.org/))
- ✅ **Azure OpenAI API** credentials (or OpenAI API key)
- ✅ **Terminal/Command Prompt** access
- ✅ **Code Editor** (VS Code recommended)

### Check Your Installations

```bash
# Check Python version
python --version  # or python3 --version

# Check Node.js version
node --version

# Check npm version
npm --version
```

---

## 🔧 Step 1: Configure Azure OpenAI

### 1.1 Update Configuration File

Navigate to the project root and edit `config.py`:

```bash
cd AI_Teaching_Assistant_from_scratch
```

Edit `config.py` with your credentials:

```python
# config.py
AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
AZURE_OPENAI_API_KEY = "your-api-key-here"
AZURE_OPENAI_API_VERSION = "2024-02-15-preview"
GPT4_DEPLOYMENT_NAME = "gpt-4"  # Your deployment name
```

⚠️ **Important:** Never commit API keys to version control!

---

## 🐍 Step 2: Setup Backend (FastAPI)

### 2.1 Navigate to Backend Folder

```bash
cd 09_complete_ui/backend
```

### 2.2 Create Virtual Environment (Recommended)

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 2.3 Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `openai` - Azure OpenAI SDK
- `pydantic` - Data validation

### 2.4 Start the Backend Server

```bash
uvicorn api:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 2.5 Test the Backend

Open your browser and visit:
- **API Root:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs (Interactive Swagger UI)
- **Health Check:** http://localhost:8000/health

✅ **Backend is ready!** Keep this terminal running.

---

## ⚛️ Step 3: Setup Frontend (React)

### 3.1 Open a New Terminal

Keep the backend terminal running and open a **new terminal window**.

### 3.2 Navigate to Frontend Folder

```bash
cd AI_Teaching_Assistant_from_scratch/09_complete_ui/frontend
```

### 3.3 Install Node Dependencies

```bash
npm install
```

This installs:
- `react` & `react-dom` - UI library
- `typescript` - Type safety
- `tailwindcss` - CSS framework
- `framer-motion` - Animations
- `axios` - HTTP client
- `vite` - Build tool

**Note:** This may take a few minutes on first install.

### 3.4 Create Environment File

```bash
cp .env.example .env
```

The `.env` file should contain:
```env
VITE_API_URL=http://localhost:8000
```

### 3.5 Start the Frontend Dev Server

```bash
npm run dev
```

You should see:
```
  VITE v5.0.8  ready in 500 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

### 3.6 Open the Application

Open your browser and visit: **http://localhost:3000**

✅ **Frontend is ready!** You should see the beautiful AI Teaching Assistant UI.

---

## 🎉 Step 4: Test the Application

### 4.1 Try These Test Messages

1. **Chat Agent Test:**
   - Type: "What is Python?"
   - Should see blue badge: 💬 Chat Agent

2. **Quiz Agent Test:**
   - Type: "Create a quiz on machine learning"
   - Should see green badge: 📝 Quiz Agent

3. **Explanation Agent Test:**
   - Type: "Explain how neural networks work"
   - Should see purple badge: 🧠 Explanation Agent

### 4.2 Check Features

- ✅ Messages appear with smooth animations
- ✅ Agent badges show which agent responded
- ✅ Markdown formatting works
- ✅ Sidebar shows agent information
- ✅ Clear chat button works
- ✅ Responsive design (try resizing window)

---

## 🐛 Troubleshooting

### Backend Issues

#### Problem: "Module not found" error
**Solution:**
```bash
# Make sure you're in the backend folder
cd 09_complete_ui/backend

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problem: "Address already in use" (Port 8000)
**Solution:**
```bash
# Kill the process using port 8000
# macOS/Linux:
lsof -ti:8000 | xargs kill -9

# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or use a different port:
uvicorn api:app --reload --port 8001
```

#### Problem: "Azure OpenAI authentication failed"
**Solution:**
- Check your `config.py` has correct credentials
- Verify your Azure OpenAI resource is active
- Check your API key hasn't expired
- Ensure deployment name matches your Azure setup

### Frontend Issues

#### Problem: "npm install" fails
**Solution:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

#### Problem: "Port 3000 already in use"
**Solution:**
```bash
# Kill the process using port 3000
# macOS/Linux:
lsof -ti:3000 | xargs kill -9

# Windows:
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# Or use a different port:
npm run dev -- --port 3001
```

#### Problem: "Cannot connect to backend"
**Solution:**
1. Ensure backend is running on port 8000
2. Check `.env` file has correct API URL
3. Check browser console for CORS errors
4. Verify backend CORS settings in `api.py`

#### Problem: Styling looks broken
**Solution:**
```bash
# Rebuild Tailwind CSS
npm run build

# Restart dev server
npm run dev
```

---

## 📁 Project Structure Reference

```
09_complete_ui/
├── backend/                    # FastAPI Backend
│   ├── api.py                 # Main API file
│   ├── requirements.txt       # Python dependencies
│   └── venv/                  # Virtual environment (created)
│
├── frontend/                   # React Frontend
│   ├── src/                   # Source code
│   ├── node_modules/          # Node dependencies (created)
│   ├── package.json           # Node dependencies list
│   └── .env                   # Environment variables (create this)
│
├── orchestrator.py            # Agent coordinator
├── chat_agent.py             # Chat agent
├── quiz_agent.py             # Quiz agent
└── explanation_agent.py      # Explanation agent
```

---

## 🔄 Development Workflow

### Daily Development

**Terminal 1 - Backend:**
```bash
cd AI_Teaching_Assistant_from_scratch/09_complete_ui/backend
source venv/bin/activate  # Activate virtual environment
uvicorn api:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd AI_Teaching_Assistant_from_scratch/09_complete_ui/frontend
npm run dev
```

### Making Changes

**Backend Changes:**
- Edit files in `backend/` or parent folder (agents, orchestrator)
- FastAPI auto-reloads with `--reload` flag
- Check terminal for errors

**Frontend Changes:**
- Edit files in `frontend/src/`
- Vite auto-reloads (Hot Module Replacement)
- Check browser console for errors

---

## 🚀 Production Build

### Build Frontend for Production

```bash
cd frontend
npm run build
```

This creates an optimized build in `frontend/dist/`

### Run Production Preview

```bash
npm run preview
```

---

## 📚 Useful Commands

### Backend Commands
```bash
# Start backend
uvicorn api:app --reload

# Start on different port
uvicorn api:app --reload --port 8001

# Start with custom host
uvicorn api:app --reload --host 0.0.0.0

# View API docs
open http://localhost:8000/docs
```

### Frontend Commands
```bash
# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linter
npm run lint
```

---

## 🎯 Next Steps

Once everything is running:

1. ✅ **Explore the UI** - Try different types of questions
2. ✅ **Check API Docs** - Visit http://localhost:8000/docs
3. ✅ **Modify Code** - Make changes and see live updates
4. ✅ **Customize Design** - Edit Tailwind colors and styles
5. ✅ **Add Features** - Extend with new agents or UI components

---

## 💡 Tips

- **Use VS Code:** Great for both Python and TypeScript
- **Install Extensions:** Python, ESLint, Tailwind CSS IntelliSense
- **Keep Terminals Visible:** Monitor both backend and frontend logs
- **Use Browser DevTools:** Check Network tab for API calls
- **Read Error Messages:** They usually tell you exactly what's wrong

---

## 🆘 Still Having Issues?

1. **Check Prerequisites:** Ensure Python and Node.js are installed
2. **Read Error Messages:** They contain helpful information
3. **Check Ports:** Make sure 8000 and 3000 are available
4. **Verify Config:** Double-check `config.py` and `.env`
5. **Restart Everything:** Sometimes a fresh start helps

---

## ✅ Success Checklist

- [ ] Python 3.8+ installed
- [ ] Node.js 18+ installed
- [ ] Azure OpenAI credentials configured
- [ ] Backend dependencies installed
- [ ] Backend running on port 8000
- [ ] Frontend dependencies installed
- [ ] Frontend running on port 3000
- [ ] Can send messages and get responses
- [ ] All three agents working
- [ ] UI looks beautiful with animations

---

**🎉 Congratulations! You're ready to build amazing AI applications!**

For more help, check:
- `README.md` in each folder
- API documentation at http://localhost:8000/docs
- Frontend README at `frontend/README.md`

