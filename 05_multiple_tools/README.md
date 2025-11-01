# Step 5: Multiple Tools

## 🎯 What You'll Learn

Give the AI **multiple tools** and watch it choose the right one:
- How to define multiple tools
- How AI selects the appropriate tool
- How to handle multiple function calls
- Building a more capable assistant

---

## 🧠 Key Concepts

### Multiple Tools = More Capabilities
Instead of one tool, give the AI several:
- `generate_quiz()` - Create quizzes
- `explain_concept()` - Explain topics
- `assess_answer()` - Grade student answers

The AI will choose which tool to use based on the user's request!

---

## 🚀 How to Run

```bash
python multiple_tools.py
```

---

## 💡 What to Observe

Try different requests:
- "Create a quiz on Python" → Uses `generate_quiz()`
- "Explain machine learning" → Uses `explain_concept()`
- "Grade this answer: ..." → Uses `assess_answer()`

The AI automatically picks the right tool!

---

## ➡️ Next Step

```bash
cd ../06_single_agent
```

