import sys
import pygame

def drawScreen():
    # Initialize Pygame
    pygame.init()

    # Set the display mode to a small screen (e.g. 640x480)
    screen = pygame.display.set_mode((640, 480))

    # Set the title of the window
    pygame.display.set_caption("Small Screen")

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with a color (e.g. black)
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        pygame.time.Clock().tick(60)

def main():
    pass



if __name__ == "__main__":
    drawScreen()
