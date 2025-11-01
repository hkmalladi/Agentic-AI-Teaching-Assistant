# Step 8: Orchestrator

**📦 This folder is self-contained!** All agent files (chat_agent.py, quiz_agent.py, explanation_agent.py) are included here - no need to reference other folders.

## 🎯 What You'll Learn

Create an **orchestrator** to coordinate multiple agents:
- What an orchestrator is
- How to route requests to the right agent
- How to coordinate multiple agents
- The orchestrator pattern

---

## 🧠 Key Concepts

### 1. **The Problem**
In Step 7, we had 3 agents:
- ChatAgent
- QuizAgent
- ExplanationAgent

**Problem:** How do we know which agent to use for each request?

### 2. **The Solution: Orchestrator**
The orchestrator is like a **traffic controller**:
- Receives all user requests
- Determines which agent should handle it
- Routes to the appropriate agent
- Returns the result

### 3. **The Orchestrator Pattern**
```
User Request
     ↓
Orchestrator (decides which agent)
     ↓
   ┌─┴─┐
   ↓   ↓   ↓
Chat Quiz Explain
   ↓   ↓   ↓
   └─┬─┘
     ↓
  Response
```

---

## 📝 The Code

`orchestrator.py` demonstrates:
1. Creating an orchestrator class
2. Initializing all agents
3. Routing logic (which agent to use)
4. Processing requests through agents
5. Returning results

---

## 🚀 How to Run

```bash
python orchestrator.py
```

---

## 💡 What to Observe

Watch how the orchestrator routes different requests:

1. **"What is Python?"** → Routes to ChatAgent
2. **"Create a quiz on ML"** → Routes to QuizAgent
3. **"Explain photosynthesis"** → Routes to ExplanationAgent

The orchestrator automatically picks the right agent!

---

## 🔬 Experiment!

### Experiment 1: Test Routing
Try different requests and see which agent is chosen:

```python
orchestrator.process_request("Hello!")  # Chat?
orchestrator.process_request("Quiz me on Python")  # Quiz?
orchestrator.process_request("Explain variables")  # Explanation?
```

### Experiment 2: Add a New Agent
Add a 4th agent and update the orchestrator:

```python
class AssessmentAgent:
    """Grades answers"""
    pass

# In orchestrator
self.assessment_agent = AssessmentAgent()
```

### Experiment 3: Improve Routing
Make the routing logic smarter:

```python
# Use keywords
if "quiz" in user_message.lower():
    return "quiz"
elif "explain" in user_message.lower():
    return "explanation"
```

---

## 🎓 Teaching Points

### For Students:
- Orchestrator coordinates multiple agents
- Routing can be rule-based or AI-based
- This is a common design pattern
- Used in production systems

### For Instructors:
- Show how routing works
- Demonstrate with different requests
- Explain design pattern benefits
- Discuss alternative approaches

---

## 🔑 Key Takeaways

1. **Orchestrator = Coordinator:**
   - Single entry point for all requests
   - Routes to appropriate agent
   - Manages agent lifecycle

2. **Routing strategies:**
   - **Rule-based:** Keywords, patterns
   - **AI-based:** Use GPT to decide
   - **Hybrid:** Combine both

3. **Benefits:**
   - Clean separation of concerns
   - Easy to add/remove agents
   - Centralized control
   - Testable routing logic

4. **This is professional architecture:**
   - Used in microservices
   - Used in AI systems
   - Industry standard pattern

---

## 🏗️ Architecture

```
Orchestrator Pattern
┌─────────────────────────────────┐
│        Orchestrator             │
│  ┌──────────────────────────┐  │
│  │  Routing Logic           │  │
│  │  (Determines which agent)│  │
│  └──────────────────────────┘  │
│                                 │
│  ┌──────┐ ┌──────┐ ┌──────┐   │
│  │Chat  │ │Quiz  │ │Explain│   │
│  │Agent │ │Agent │ │Agent  │   │
│  └──────┘ └──────┘ └──────┘   │
└─────────────────────────────────┘
```

---

## 💻 Real-World Applications

Orchestrators are used in:
- **Microservices:** API gateway routes to services
- **AI Systems:** Route to specialized models
- **Customer Service:** Route to department
- **Smart Assistants:** Route to skills (Alexa, Google)

---

## 🎯 Routing Strategies

### 1. **Keyword-Based (Simple)**
```python
if "quiz" in message:
    return "quiz"
```
**Pros:** Fast, predictable
**Cons:** Limited, brittle

### 2. **AI-Based (Smart)**
```python
# Use GPT to decide
response = gpt("Which agent should handle this?")
```
**Pros:** Flexible, intelligent
**Cons:** Slower, costs tokens

### 3. **Hybrid (Best)**
```python
# Try keywords first
if "quiz" in message:
    return "quiz"
# Fall back to AI
else:
    return ai_route(message)
```
**Pros:** Fast + Smart
**Cons:** More complex

---

## ⚡ Performance Tips

1. **Cache routing decisions** for common requests
2. **Use keywords** for obvious cases
3. **Use AI** for ambiguous cases
4. **Monitor** which agents are used most
5. **Optimize** the most-used paths

---

## ➡️ Next Step

Now that you have an orchestrator coordinating multiple agents, it's time to add a **user interface**!

Move to **Step 9: Complete UI** to build a web interface with Streamlit.

```bash
cd ../09_complete_ui
streamlit run app.py
```

---

## 🤔 Common Questions

**Q: Can I have multiple orchestrators?**
A: Yes! You could have orchestrators for different domains.

**Q: Should the orchestrator have its own logic?**
A: Minimal. It should mostly route, not process.

**Q: What if routing is wrong?**
A: Add fallback logic or let users choose.

**Q: Can agents call other agents?**
A: Better to go through the orchestrator for coordination.

---

**Ready? Run the orchestrator and see intelligent routing in action! 🚀**

