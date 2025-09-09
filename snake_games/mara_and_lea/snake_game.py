import pygame
import sys

# --- Game Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20 # Each segment of the snake and food will be 20x20 pixels

# Colors (RGB tuples)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0) # Snake color
RED = (255, 0, 0)   # Food color
BLUE = (0, 0, 255)  # UI color
GRAY = (100, 100, 100) # For inactive input box
LIGHT_GRAY = (200, 200, 200) # For active input box border

# Snake movement directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game speed (frames per second)
# We will define speeds for selection in the UI later
INITIAL_SNAKE_SPEED = 10 # Default speed, will be overridden by user selection

# --- Speed Options ---
SPEED_OPTIONS = {
    "Slow": 5,
    "Medium": 10,
    "Fast": 15
}
SPEED_KEYS = list(SPEED_OPTIONS.keys()) # For cycling through options

# --- Game States ---
STATE_MENU = 0
STATE_PLAYING = 1
STATE_GAME_OVER = 2

# --- Game Configuration for Deterministic Play ---
# The snake's starting position (head)
STARTING_SNAKE_POSITION = (5, 5) # (x, y) grid coordinates

# Deterministic food placement (list of (x, y) grid coordinates)
# The food will appear in this sequence
FOOD_POSITIONS = [
    (10, 10),
    (15, 5),
    (7, 12),
    (20, 8),
    (3, 18),
]

# --- Main Game Function ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Nokia Snake")
    clock = pygame.time.Clock()

    # --- Game State Variable ---
    game_state = STATE_MENU

    # --- Game Variables (will be initialized/reset based on game state) ---
    snake = []
    direction = RIGHT
    food_index = 0
    food_pos = None
    score = 0
    game_over = False 

    # --- UI Variables ---
    username = "Player1" # Default username
    current_speed_idx = 1 # Start at "Medium" speed
    selected_speed = SPEED_OPTIONS[SPEED_KEYS[current_speed_idx]]
    input_active = False # For username input

    # --- Font for Score and Game Over Message ---
    font_small = pygame.font.Font(None, 25) # Default font, size 25
    font_medium = pygame.font.Font(None, 40) # Default font, size 40 (for menu items)
    font_large = pygame.font.Font(None, 75) # Default font, size 75

    # --- UI Element Rects (for click detection and positioning) ---
    # Username input box
    username_input_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 40)
    
    # Speed selection
    speed_text_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 40)
    
    # Start button
    start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 100, 150, 50)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            if game_state == STATE_MENU:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if username_input_rect.collidepoint(event.pos):
                        input_active = not input_active
                    else:
                        input_active = False
                    
                    # Handle speed selection clicks
                    if speed_text_rect.collidepoint(event.pos):
                        current_speed_idx = (current_speed_idx + 1) % len(SPEED_KEYS)
                        selected_speed = SPEED_OPTIONS[SPEED_KEYS[current_speed_idx]]

                    # Handle start button click
                    if start_button_rect.collidepoint(event.pos):
                        # Reset game variables for a new game
                        snake = [
                            STARTING_SNAKE_POSITION,
                            (STARTING_SNAKE_POSITION[0] - 1, STARTING_SNAKE_POSITION[1]),
                            (STARTING_SNAKE_POSITION[0] - 2, STARTING_SNAKE_POSITION[1]),
                        ]
                        direction = RIGHT
                        food_index = 0
                        food_pos = FOOD_POSITIONS[food_index]
                        score = 0
                        
                        game_state = STATE_PLAYING # Start the game!

                if event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    elif event.key == pygame.K_RETURN: # Enter key deactivates input
                        input_active = False
                    else:
                        if len(username) < 15: # Limit username length
                            username += event.unicode
            
            # Event handling for PLAYING state will move here (existing snake controls)
            elif game_state == STATE_PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != DOWN:
                        direction = UP
                    elif event.key == pygame.K_DOWN and direction != UP:
                        direction = DOWN
                    elif event.key == pygame.K_LEFT and direction != RIGHT:
                        direction = LEFT
                    elif event.key == pygame.K_RIGHT and direction != LEFT:
                        direction = RIGHT
            
            # Event handling for GAME_OVER state (restart button) will go here later

        # --- Game Logic and Drawing (state-dependent) ---
        screen.fill(BLACK) 

        if game_state == STATE_MENU:
            # Draw Title
            title_text = font_large.render("Nokia Snake", True, WHITE)
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
            screen.blit(title_text, title_rect)

            # Draw Username Input
            username_label = font_medium.render("Username:", True, WHITE)
            username_label_rect = username_label.get_rect(midright=(username_input_rect.left - 10, username_input_rect.centery))
            screen.blit(username_label, username_label_rect)

            pygame.draw.rect(screen, LIGHT_GRAY if input_active else GRAY, username_input_rect, 0 if input_active else 2) # Fill if active, border if not
            username_surface = font_medium.render(username, True, WHITE)
            screen.blit(username_surface, (username_input_rect.x + 5, username_input_rect.y + 5))
            
            # Draw Speed Selection
            speed_label = font_medium.render("Speed:", True, WHITE)
            speed_label_rect = speed_label.get_rect(midright=(speed_text_rect.left - 10, speed_text_rect.centery))
            screen.blit(speed_label, speed_label_rect)
            
            speed_option_text = font_medium.render(SPEED_KEYS[current_speed_idx], True, BLUE)
            speed_option_text_rect = speed_option_text.get_rect(center=speed_text_rect.center)
            screen.blit(speed_option_text, speed_option_text_rect)
            pygame.draw.rect(screen, BLUE, speed_text_rect, 2) # Border

            # Draw Start Button
            pygame.draw.rect(screen, GREEN, start_button_rect)
            start_text = font_medium.render("Start Game", True, BLACK)
            start_text_rect = start_text.get_rect(center=start_button_rect.center)
            screen.blit(start_text, start_text_rect)

        elif game_state == STATE_PLAYING:
            # Game logic for playing state (moved from original main loop)
            # Calculate new head position
            head_x, head_y = snake[0]
            dir_x, dir_y = direction
            new_head = (head_x + dir_x, head_y + dir_y)

            # --- Collision Detection ---
            # Wall collision
            if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH // CELL_SIZE or
                new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT // CELL_SIZE):
                game_state = STATE_GAME_OVER # Transition to Game Over
            
            # Self-collision (check if new_head is in the rest of the snake's body)
            if new_head in snake[1:]: 
                game_state = STATE_GAME_OVER # Transition to Game Over

            if game_state == STATE_PLAYING: # Only update snake if no collision occurred
                # Insert new head
                snake.insert(0, new_head)

                # Check if food was eaten
                if new_head == food_pos:
                    score += 1
                    food_index += 1
                    if food_index < len(FOOD_POSITIONS):
                        food_pos = FOOD_POSITIONS[food_index]
                    else:
                        game_state = STATE_GAME_OVER # End game if all deterministic food is collected
                else:
                    # If no food was eaten, remove the tail
                    snake.pop()

            # Drawing for playing state (moved from original main loop)
            # Draw snake
            for segment in snake:
                pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Draw food
            if food_pos is not None: # Only draw food if it exists (not collected all)
                pygame.draw.rect(screen, RED, (food_pos[0] * CELL_SIZE, food_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Display Score
            score_text = font_small.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (5, 5)) # Top-left corner

        elif game_state == STATE_GAME_OVER:
            # Drawing and logic for the game over screen will go here (final score, highscore, restart button)
            pass

        pygame.display.flip()
        clock.tick(selected_speed if game_state == STATE_PLAYING else INITIAL_SNAKE_SPEED) 

    pygame.quit()
    sys.exit() 

if __name__ == '__main__':
    main() 