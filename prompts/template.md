## Prompt Template

Use this template to curtomize your LLM prompt accordingly to the following techniques: rephrase & respond, chain of thought (plan-then-code), chain of knowledge, reflection, self-consistency, and more.
The "[]" is a placeholder for your individual task. Pleas insert the neccessary information.


### 1) Chain of thought 

Prompt:
```
[]. Please explain your thought process step-by-step as you develop the answer.

```

---

### 2) Chain of knowledge

Prompt:
```
[]. Please list key facts and relevant [programming] concepts required for the result as you develop your answer step-by-step.
```

---

---

### 3) Reflection

Prompt:
```
[]. Please self-review your answer for [mistakes, bugs, edge cases, missing features].
```

---

### 4) Self-consistency

Prompt:
```
Generate [two/three] alternative [implementations/solutions] of []. Compare them with pros/cons [performance/clarity/bug risk]. Choose the better one for [beginners/advanced users] and apply it.
```

---


### 5) Rephrase & respond


Prompt:
```
Please restate the following task so that it includes all neccessary instructions in order to write functional code: []. You can add missing polishing items as a checklist [e.g. ...].
```

---
