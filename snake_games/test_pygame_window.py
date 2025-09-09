import pygame

def main():
    # Initialize all the Pygame modules
    pygame.init()

    # Set up the display (window)
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Test Window")

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check if the user clicked the close button
                running = False

        # Drawing (optional, just filling the background)
        screen.fill((0, 0, 0)) # Fill the screen with black

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    main() 