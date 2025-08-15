## Cursor Prompt Pack: Python Snake Game (Pygame)

Use these copy‑paste prompts in Cursor to build a complete Snake game in Python. They are organized by phase and demonstrate prompting techniques: rephrase & respond, chain of thought (plan-then-code), chain of knowledge, reflection, self-consistency, and more.

Notes for facilitators:
- Designed for absolute beginners; no prior coding required.
- Works best with Python 3.10+ and `pygame`.
- Encourage participants to paste prompts verbatim, then iterate.

---

### 1) Rephrase & Clarify the Task

**Goal:** Align on scope and constraints before anything else.
**Technique:** Rephrase & Respond 

Prompt:
```
I want to build a simple Snake game in Python using pygame. Restate the task in your own words, list key constraints (beginner-friendly, minimal dependencies, readable code), 
and write 5–7 clarifying questions about scope (grid size, controls, restart behavior, scoring, file layout). Finish with a short, bullet outline of the core components we’ll need. Do NOT write any code.
```

---

### 2) Generate first Implementation Plan 

**Goal:** Produce a concrete but small plan the user can approve.
**Technique:** Chain of Thoughts

Prompt:
```
Provide a brief implementation plan with 6–9 numbered steps from project bootstrap → minimal playable loop. Use this structure:
- Files to create
- Game loop responsibilities
- Core entities (snake, food, config)
- Input & collision rules
- Scoring & basic game over
Keep each step to 1 sentence. Ask me to “confirm or adjust” before coding. Do NOT write code.
```
---

### 3) Bootstrap minimal window

**Goal:** Introduce just enough pygame to open/close a window cleanly to prove the environment is ready
**Technique:** Chain of Knowledge

Prompt:
```
Briefly list the pygame basics we need (init/quit, display, event loop, Clock.tick) in 4–6 bullets. Then scaffold ONLY:
- requirements.txt (pygame)
- main.py that opens a window and closes on QUIT
Keep code very short and well-commented. No game logic yet.
```
---

### 4) Implement core entities

**Goal:** Create snake, food, and config with deterministic methods.
**Technique:** -

Prompt:
```
Core entities: Implement small, focused classes (no rendering yet):
- game/config.py: grid size, cell size, fps, colors
- game/snake.py: segments list, direction, move(), grow(), set_direction(), collided_with_self()
- game/food.py: position, respawn(grid_size, forbidden_positions)
Keep logic grid-based and deterministic, with lightweight docstrings. Show only these files.
```
---

### 5) Build Minimal Playable Game 

**Goal:** Wire up the first fully playable loop by assembling the previous built core entities
**Technique:** Chain of Thoughts 

Prompt:
```
First give a 6-bullet plan for a minimal playable Game class (init_window, handle_input, update, render, run). Then implement game/game.py and wire main.py to run it.
Requirements:
- Use pygame.time.Clock for FPS
- Spawn food off-snake
- Eat food → grow + score++
- Detect wall or self collision → game over state, R to restart

Keep rendering simple rectangles; no fonts or HUD yet.
```

---

### 6) Quality Check and Bug-Prevention

**Goal:** Catch common pitfalls and fix small issues.  
**Technique:** Reflection 

Prompt:
```
Check and fix if necessary:
- pygame init/quit correctness
- Direction change guard: prevent 180° reversal within one tick
- Clear separation: update vs render
- Magic numbers centralized in config
- Clean restart state on game over (R)

Report changes in 4–6 bullets, then show diffs only.
```
---

### 7) Add Simple User-Interface

**Goal:** Minimal UI without performance regressions 
**Technique:** -  

Prompt:
```
Add a simple UI:
- Top-left: Score
- Bottom-center: "Arrows to move • R to restart"

Use pygame.font (initialize once), render efficiently, and keep draw code clean. Show only changed files.
```
---

### 8) Brainstorm & Add Features

**Goal:** Encourage creativity while keeping changes safe.  
**Technique:** Chain of Knowledge  

Prompt:
```
Propose 4 small, beginner-friendly features (e.g., pause with P, wrap-around mode, speed ramp every N apples, grid border). Give 1–2 sentence rationale for each. 
Choose the best 1–2 for now (favor clarity and low bug risk), then implement them with minimal diffs and a 5-step manual test plan.
```
---

### 9) Final Tidy & Run Instructions

**Goal:** Clean up code and make it easy to run.  
**Technique:** Self-consistency review

Prompt:
```
- In 8 bullets max, review naming, function sizes, separation of concerns, configurability, and robustness.
- Apply the 3 most impactful cleanups (show diffs only).
- Provide a short "How to run" section (venv steps for Win/macOS/Linux, pip install -r requirements.txt, python main.py) and a brief troubleshooting note for common pygame issues.

```

