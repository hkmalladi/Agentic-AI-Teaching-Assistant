# Step 1: Basic Prompt

## 🎯 What You'll Learn

In this step, you'll learn the **absolute basics** of interacting with GPT-4:
- How to send a prompt to the AI
- What a system prompt is
- What a user prompt is
- How to get a response

This is the foundation for everything else!

---

## 🧠 Key Concepts

### 1. **System Prompt**
Instructions that define the AI's behavior and role.

**Example:**
```python
"You are a helpful teaching assistant who explains concepts clearly."
```

This tells the AI **how to behave** - be helpful, be a teacher, explain clearly.

### 2. **User Prompt**
The actual question or request from the user.

**Example:**
```python
"What is photosynthesis?"
```

This is **what the user wants** - an explanation of photosynthesis.

### 3. **Messages List**
The format Azure OpenAI expects - a list of message objects.

**Format:**
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is Python?"}
]
```

---

## 📝 The Code

The code in `basic_prompt.py` does three things:

1. **Initialize** the Azure OpenAI client
2. **Create** a messages list with system and user prompts
3. **Send** the request and print the response

---

## 🚀 How to Run

```bash
python basic_prompt.py
```

---

## 💡 What to Observe

When you run the code, notice:

1. **The system prompt** defines the AI's role as a teaching assistant
2. **The user prompt** asks a specific question
3. **The response** follows the style defined in the system prompt
4. **The time** it takes to get a response

---

## 🔬 Experiment!

Try modifying the code:

### Experiment 1: Change the System Prompt
```python
# Try this:
"You are a pirate who teaches students. Always use pirate language."

# Or this:
"You are a professor who uses very formal academic language."
```

**Question:** How does the response change?

### Experiment 2: Change the User Prompt
```python
# Try asking different questions:
"Explain quantum physics"
"What is the capital of France?"
"How do I write a for loop in Python?"
```

**Question:** Does the AI maintain the teaching assistant style?

### Experiment 3: Change the Temperature
```python
# In the code, find this line:
temperature=0.7

# Try different values:
temperature=0.0  # More focused and deterministic
temperature=1.0  # More creative and varied
```

**Question:** How does temperature affect the response?

---

## 📊 Understanding the Response

The API returns a response object with this structure:

```python
response.choices[0].message.content  # The actual text response
```

- `choices` - List of possible responses (usually just one)
- `[0]` - The first (and usually only) response
- `message.content` - The actual text

---

## 🎓 Teaching Points

### For Students:
- This is the simplest way to interact with AI
- System prompts are powerful - they shape the AI's behavior
- User prompts should be clear and specific

### For Instructors:
- Start here to demystify AI APIs
- Show how simple the basic interaction is
- Demonstrate the power of system prompts
- Let students experiment with different prompts

---

## 🔑 Key Takeaways

1. **Two types of prompts:**
   - System prompt = How the AI should behave
   - User prompt = What the user wants

2. **Messages format:**
   - Always a list of dictionaries
   - Each has a "role" and "content"

3. **Simple interaction:**
   - Initialize client
   - Create messages
   - Get response

4. **System prompts matter:**
   - They define the AI's personality and behavior
   - They persist across the conversation

---

## ➡️ Next Step

Once you understand basic prompts, move to **Step 2: Conversation History** to learn how to maintain context across multiple messages.

```bash
cd ../02_conversation_history
cat README.md
```

---

## 🤔 Common Questions

**Q: Why do we need a system prompt?**
A: It sets the context and behavior for the AI. Without it, the AI might not know how to respond appropriately.

**Q: Can I have multiple user messages?**
A: Yes! That's what we'll learn in Step 2 (Conversation History).

**Q: What's the difference between temperature 0 and 1?**
A: Temperature 0 is deterministic (same input = same output). Temperature 1 is more creative and varied.

**Q: How long can prompts be?**
A: GPT-4 can handle very long prompts (thousands of tokens), but shorter is usually better.

---

## 📚 Additional Resources

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

---

**Ready? Run the code and see it in action! 🚀**

