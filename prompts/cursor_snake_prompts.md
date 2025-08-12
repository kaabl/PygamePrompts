## Cursor Prompt Pack: Python Snake Game (Pygame)

Use these copy‑paste prompts in Cursor to build a complete Snake game in Python. They are organized by phase and demonstrate prompting techniques: rephrase & respond, chain of thought (plan-then-code), chain of knowledge, reflection, self-consistency, and more.

Notes for facilitators:
- Designed for absolute beginners; no prior coding required.
- Works best with Python 3.10+ and `pygame`.
- Encourage participants to paste prompts verbatim, then iterate.

---

### 0) Kickoff: Rephrase & respond

Goal: Ensure the AI fully understands the task and constraints.

Prompt:
```
Rephrase & respond: I want to build a simple, playable Snake game in Python using pygame. Restate the task in your own words, list key components we will need (files, functions, modules), and propose a minimal initial plan with 5–8 steps. Then ask me to confirm or adjust the plan before coding. Limit the response to a concise outline.
```

---

### 1) Plan-then-code: Chain of thought (structured)

Goal: Get a clear plan before writing code. Ask for a “Plan → Code” structure (do not dump long reasoning; keep it concise).

Prompt:
```
Plan then code: Provide a brief, numbered implementation plan for the Snake game based on our agreed scope. Use this structure:
- Plan: 5–10 bullet steps, each 1 sentence
- Code: only the files needed to run a minimal playable version
Constraints:
- Use pygame
- Files: main.py (entry point), game/snake.py, game/food.py, game/config.py, game/game.py
- Include a simple game loop, grid, snake movement, food spawning, collision detection, scoring, and game over
- Keep code readable with meaningful names and small functions
After the code, provide a "How to run" section with pip install and run instructions.
```

---

### 2) Project bootstrap (chain of knowledge)

Goal: Have the AI leverage relevant knowledge (e.g., pygame basics) and provide citations/links when helpful.

Prompt:
```
Chain of knowledge: Before coding, list the minimal pygame concepts required (window setup, clock/tick, event handling, surfaces, rects). Provide short explanations and, if helpful, include official doc links. Then proceed to scaffold the project structure and a basic window that closes cleanly.
Deliverables:
- requirements.txt (with pygame)
- main.py that opens a window and exits on QUIT
- README snippet: quick start instructions
```

---

### 3) Implement core entities (snake, food, config)

Goal: Build out minimal data structures with simple, testable methods.

Prompt:
```
Implement core entities using small, focused classes:
- game/config.py: grid size, cell size, fps, colors
- game/snake.py: Snake segments list, direction, move(), grow(), set_direction(), collided_with_self()
- game/food.py: Food position, respawn(grid_size, forbidden_positions)
Add lightweight docstrings. Keep logic deterministic and side-effect-light.
```

---

### 4) Game loop and rendering (plan → code)

Goal: Put the pieces together into a playable loop.

Prompt:
```
Plan then code: Implement game/game.py with a Game class that encapsulates:
- init_window()
- handle_input()
- update()
- render()
- run()
Responsibilities:
- Use pygame.time.Clock for consistent FPS
- Spawn food not on the snake
- Increase score on eat; respawn food
- Detect wall and self collisions → game over state with restart option (press R)
Finally, wire main.py to run Game().run().
```

---

### 5) Reflection: quick QA checklist

Goal: Ask the AI to self-review for common pitfalls.

Prompt:
```
Reflection: Review the current code against this checklist and fix issues you find:
- Are pygame init/quit calls correct? Any resource leaks?
- Is input handling debounced (no direction reversal into itself in one tick)?
- Is rendering separated from game state updates?
- Are magic numbers centralized in config?
- Does the game over flow work reliably (restart returns to a clean state)?
Report the changes briefly, then show updated diffs.
```

---

### 6) Self-consistency: produce alternatives and choose

Goal: Generate 2–3 variants for a tricky function, compare, pick the best.

Prompt:
```
Self-consistency: Generate two alternative implementations of the snake movement and turning logic that prevent 180° reversals and handle buffered input cleanly. Compare them with pros/cons (performance, clarity, bug risk). Choose the better one for beginners and apply it. Show only the changed code.
```

---

### 7) Add scoring UI and simple HUD

Goal: Display score and instructions on screen.

Prompt:
```
Add a simple HUD:
- Top-left: score
- Top-right: FPS
- Bottom-center (small): controls (Arrow keys to move, R to restart)
Use pygame.font. Ensure fonts initialize once and performance is smooth. Update only necessary parts of the screen if you optimize.
```

---

### 8) Rephrase & respond: constraints and polish

Goal: Reinforce constraints and polish requirements.

Prompt:
```
Rephrase & respond: Restate our project’s current state and the remaining polish items as a checklist. Confirm constraints: no external assets, minimal dependencies, readable code, and consistent frame timing. Propose a short list of polish tasks (e.g., pause toggle, speed ramp, grid border). Ask me to choose 1–2 to implement now.
```

---

### 9) Chain of knowledge: small feature extensions

Goal: Add one or two beginner-friendly extensions with brief rationale.

Prompt:
```
Chain of knowledge: Suggest 3 small features suitable for beginners (e.g., pause with P, gradual speed increase every N apples, wrap-around mode). For the chosen feature(s), briefly explain the concept, then implement with clear code and minimal changes. Provide a short test plan (manual steps) to verify.
```

---

### 10) Debugging loop: guided reflection prompts

Goal: Provide prompts to diagnose common issues.

Prompts:
```
Reflection (input handling): If the snake reverses into itself on fast direction changes, locate where direction is updated versus when the movement tick occurs. Propose a buffered input approach or a "next_direction" variable with guard rails. Apply the fix and explain the change in 2–3 sentences.
```

```
Reflection (collision): If wall or self-collision detection is unreliable, show the exact condition checks and the coordinate system assumptions (grid vs pixels). Unify on grid coordinates and centralize conversions in config.
```

```
Reflection (performance): If FPS is unstable, verify Clock.tick usage, rendering cost (avoid expensive per-frame ops), and font rendering frequency. Cache surfaces where possible.
```

---

### 11) Self-consistency: code review snapshot

Goal: Have the AI produce a short code review and address findings.

Prompt:
```
Self-consistency code review: In 8–12 bullet points, review the code for naming clarity, function size, separation of concerns, configurability, and robustness. Propose concrete improvements and apply the top 3 that have the biggest impact for beginners learning from this codebase. Show diffs only.
```

---

### 12) Packaging and running instructions

Goal: Make it easy to run on Windows, macOS, Linux.

Prompt:
```
Provide a concise "How to run" section suitable for the README:
- Python version requirement
- Create and activate venv (Windows/macOS/Linux)
- pip install -r requirements.txt
- python main.py
Add a troubleshooting section for common pygame issues (e.g., missing SDL, font issues), each with one-line fixes.
```

---

### 13) Final reflection and handoff

Goal: Summarize what was learned and next steps.

Prompt:
```
Final reflection: Summarize the key prompting techniques we used (rephrase & respond, plan-then-code chain of thought, chain of knowledge, reflection, self-consistency). Provide 5 suggested next steps for learners (e.g., add sound effects, menu screen, high scores file, unit tests for snake logic, difficulty levels). Keep it concise.
```

---

### Optional: Testing the core logic (no graphics)

Goal: Encourage testable design by isolating logic from pygame.

Prompt:
```
Create a tests/ folder with simple pytest tests for snake movement, growth, and self-collision on a small grid. Ensure core logic is grid-based and independent from pygame surfaces so tests run headless. Update instructions to include pytest in requirements and how to run tests.
```

---

### Facilitator tips (meta)

- Encourage participants to skim the AI’s plan before accepting code.
- If the AI produces too much code at once, ask it to split changes into smaller steps.
- Use “show only diffs” when iterating to keep focus.
- Prefer “Plan → Code” format to keep reasoning brief and actionable.


