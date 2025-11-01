# Step 6: Single Agent

## 🎯 What You'll Learn

Create your first **agent** - a specialized, reusable AI component:
- What an agent is
- How to encapsulate behavior
- How to make reusable components
- Agent design patterns

---

## 🧠 Key Concept: What is an Agent?

An **agent** is a self-contained component that:
1. Has a specific role/purpose
2. Maintains its own state (like conversation history)
3. Has its own system prompt
4. Can be reused independently

**Think of it as a specialized AI worker!**

---

## 📝 The Code

`chat_agent.py` demonstrates:
1. Creating an Agent class
2. Initializing with specific behavior
3. Maintaining state (conversation history)
4. Providing a clean interface

---

## 🚀 How to Run

```bash
python chat_agent.py
```

---

## 💡 What to Observe

1. **Encapsulation:** All AI logic is inside the class
2. **State management:** Agent remembers conversation
3. **Reusability:** Can create multiple instances
4. **Clean interface:** Simple `.chat()` method

---

## 🔬 Experiment!

### Experiment 1: Multiple Instances
Create multiple agents with different personalities:

```python
friendly_agent = ChatAgent()
strict_agent = ChatAgent()
# Modify strict_agent's system prompt
```

### Experiment 2: Add Methods
Add more methods to the agent:

```python
def reset_conversation(self):
    """Clear conversation history"""
    self.messages = [{"role": "system", "content": self.system_prompt}]
```

---

## 🔑 Key Takeaways

1. **Agents encapsulate behavior**
2. **Agents maintain state**
3. **Agents are reusable**
4. **Agents provide clean interfaces**

---

## ➡️ Next Step

```bash
cd ../07_multiple_agents
```

Learn how to create multiple specialized agents!

