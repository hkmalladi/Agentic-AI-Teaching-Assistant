# Step 4: Single Tool (Function Calling)

## 🎯 What You'll Learn

Learn how to give the AI a **tool** (function) it can use:
- What function calling is
- How to define a tool
- How the AI decides when to use it
- How to execute the function and return results

---

## 🧠 Key Concepts

### 1. **Function Calling**
The AI can call functions you define to get information or perform actions.

**Example:** You give the AI a `generate_quiz()` function. When a student asks for a quiz, the AI calls that function!

### 2. **The Flow**
```
1. User: "Create a quiz on Python"
2. AI thinks: "I need to call generate_quiz()"
3. AI returns: function call with parameters
4. You: Execute the function
5. You: Send results back to AI
6. AI: Formats the results for the user
```

### 3. **Tool Definition**
You define tools in a specific format:

```python
tools = [{
    "type": "function",
    "function": {
        "name": "generate_quiz",
        "description": "Generate a quiz on a topic",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "num_questions": {"type": "integer"}
            }
        }
    }
}]
```

---

## 📝 The Code

`tool_example.py` demonstrates:
1. Defining a `generate_quiz()` function
2. Telling the AI about this tool
3. AI deciding to use the tool
4. Executing the function
5. Sending results back to AI
6. AI formatting the final response

---

## 🚀 How to Run

```bash
python tool_example.py
```

---

## 💡 What to Observe

1. **User asks:** "Create a quiz on Python basics"
2. **AI decides:** "I should use generate_quiz()"
3. **AI returns:** Function call with parameters
4. **We execute:** The actual function
5. **We send back:** The quiz questions
6. **AI formats:** A nice response for the user

---

## 🔬 Experiment!

### Experiment 1: Different Questions
Try questions that should/shouldn't trigger the tool:

```python
"Create a quiz on machine learning"  # Should trigger
"What is machine learning?"          # Should NOT trigger
"Generate 10 questions about Python" # Should trigger
```

### Experiment 2: Add Parameters
Modify the tool to accept difficulty:

```python
"parameters": {
    "topic": {"type": "string"},
    "num_questions": {"type": "integer"},
    "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]}
}
```

---

## 🎓 Teaching Points

### For Students:
- AI can use tools you provide
- AI decides when to use them
- You control what functions exist
- This extends AI capabilities

### For Instructors:
- Show the tool definition format
- Demonstrate when AI chooses to use tools
- Explain the two-step process
- Discuss real-world applications

---

## 🔑 Key Takeaways

1. **Function calling = AI using tools**
2. **You define what tools exist**
3. **AI decides when to use them**
4. **Two-step process:** AI calls → You execute → AI formats

---

## ➡️ Next Step

Move to **Step 5: Multiple Tools** to give the AI multiple tools to choose from.

```bash
cd ../05_multiple_tools
```

