# Step 7: Multiple Agents

## 🎯 What You'll Learn

Create **multiple specialized agents**, each doing ONE thing well:
- **ChatAgent** - Handles conversations
- **QuizAgent** - Generates quizzes
- **ExplanationAgent** - Explains concepts

This demonstrates the **Single Responsibility Principle** - each agent has one job!

---

## 🧠 Key Concepts

### 1. **Specialized Agents**
Instead of one agent that does everything, create multiple agents:
- Each agent is an expert in its domain
- Each agent has its own system prompt
- Each agent can be developed/tested independently
- Each agent is reusable

### 2. **Single Responsibility Principle**
Each agent does ONE thing:
- ChatAgent → Conversation
- QuizAgent → Quiz generation
- ExplanationAgent → Explanations

**Why?**
- Easier to understand
- Easier to test
- Easier to improve
- More maintainable

### 3. **Agent Independence**
Each agent can work alone:
```python
# Use ChatAgent independently
chat_agent = ChatAgent()
response = chat_agent.chat("What is Python?")

# Use QuizAgent independently
quiz_agent = QuizAgent()
quiz = quiz_agent.generate_quiz("Python", 5)
```

---

## 📝 The Code

This folder has three agent files:

### `chat_agent.py`
- Handles general conversation
- Maintains conversation history
- Friendly and helpful

### `quiz_agent.py`
- Generates quizzes
- Creates multiple choice questions
- Formats questions clearly

### `explanation_agent.py`
- Explains concepts
- Provides examples
- Addresses misconceptions

---

## 🚀 How to Run

Test each agent independently:

```bash
# Test ChatAgent
python chat_agent.py

# Test QuizAgent
python quiz_agent.py

# Test ExplanationAgent
python explanation_agent.py
```

---

## 💡 What to Observe

1. **Each agent is independent**
   - Can run on its own
   - Has its own behavior
   - Doesn't depend on others

2. **Each agent is specialized**
   - ChatAgent is conversational
   - QuizAgent creates structured quizzes
   - ExplanationAgent is detailed and educational

3. **Each agent is reusable**
   - Can be imported and used anywhere
   - Can be combined with other agents
   - Can be tested independently

---

## 🔬 Experiment!

### Experiment 1: Modify Agent Behavior
Change the system prompt in one agent:

```python
# In chat_agent.py
self.system_prompt = "You are a strict teacher who gives short answers."
```

**Question:** How does this change the agent's responses?

### Experiment 2: Add a New Agent
Create a new agent:

```python
class AssessmentAgent:
    """Grades student answers"""
    def assess(self, answer, question):
        # Implementation here
        pass
```

### Experiment 3: Compare Agents
Ask the same question to different agents:

```python
chat_response = chat_agent.chat("What is machine learning?")
explanation = explanation_agent.explain("machine learning")
```

**Question:** How do the responses differ?

---

## 🎓 Teaching Points

### For Students:
- Multiple specialized agents > One general agent
- Each agent has a specific purpose
- Agents can work independently
- This is modular design

### For Instructors:
- Demonstrate each agent separately
- Show how they differ in behavior
- Explain single responsibility principle
- Discuss real-world applications

---

## 🔑 Key Takeaways

1. **Specialization is powerful:**
   - Each agent does one thing well
   - Easier to understand and maintain
   - Can be improved independently

2. **Independence is important:**
   - Agents don't depend on each other
   - Can be tested separately
   - Can be reused in different contexts

3. **Modularity enables scaling:**
   - Easy to add new agents
   - Easy to remove agents
   - Easy to modify agents

4. **This is professional design:**
   - Used in production systems
   - Industry best practice
   - Scales to large systems

---

## 🏗️ Architecture

```
Multiple Agents (Independent)
├── ChatAgent
│   ├── Purpose: Conversation
│   ├── System Prompt: Friendly assistant
│   └── State: Conversation history
├── QuizAgent
│   ├── Purpose: Quiz generation
│   ├── System Prompt: Quiz specialist
│   └── State: None (stateless)
└── ExplanationAgent
    ├── Purpose: Explanations
    ├── System Prompt: Explanation specialist
    └── State: None (stateless)
```

---

## 💻 Real-World Applications

This pattern is used in:
- **Customer service:** Different agents for billing, technical support, sales
- **Healthcare:** Different agents for diagnosis, treatment, scheduling
- **Education:** Different agents for tutoring, assessment, content creation
- **E-commerce:** Different agents for product search, recommendations, support

---

## ⚠️ Important Note

**Problem:** We now have 3 independent agents. How do we know which one to use?

**Solution:** We need an **orchestrator** to route requests to the right agent!

That's what we'll build in Step 8! 🎯

---

## ➡️ Next Step

Now that you have multiple agents, you need a way to coordinate them.

Move to **Step 8: Orchestrator** to learn how to route requests to the right agent.

```bash
cd ../08_orchestrator
cat README.md
```

---

## 🤔 Common Questions

**Q: How many agents should I have?**
A: As many as you need! Start with a few, add more as needed.

**Q: Can agents communicate with each other?**
A: Yes, but it's better to coordinate through an orchestrator.

**Q: Should all agents maintain state?**
A: Only if needed. ChatAgent needs history, but QuizAgent doesn't.

**Q: Can I have multiple instances of the same agent?**
A: Yes! You could have multiple ChatAgents for different users.

---

**Ready? Test each agent, then move to the orchestrator! 🚀**

