# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 100 | "Go lower" hint | "Go higher" hint shown | none |

| Guess incorrect number before guessing correctly | Score displayed in debug info matches score given | Debug info says score is -10 while score displayed is 40 | none |

| Switching game to easy mode | Blue instruction box says "Guess a number between 1 and 20" | Still says "Guess a number between 1 and 100" | none |

| Guess 50 first | Attempts decrease by 1, and since secret is 42 hint should say "Go lower" | Attempts don't change for first guess and hint says "Go higher" | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used ClaudeCode on this project as an agent.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One suggestion Claude gave me that was correct was that the reason the hints were off was just the string message returned for each guess. "Too Low" was paired with "Go lower!" and "Too High" was paired with "Go higher!" so I was able to fix this by switching the messages. I verified this by reading through the code myself (the logic of the hints and when they were returned) and running the game a few times.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One suggestion Claude gave me that was ____ was ____.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was fixed when I wrote tests with the help of Claude to test my fixes and they passed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.



- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
