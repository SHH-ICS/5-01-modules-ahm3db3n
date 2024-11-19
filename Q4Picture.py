import pygame
import sys

def Q4Picture():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Q4Picture")
    
    # Colors
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    
    screen.fill(WHITE)
    
    # Draw Shapes
    pygame.draw.circle(screen, RED, (200, 100), 50)  # Red Circle
    pygame.draw.rect(screen, BLUE, (100, 200, 200, 100))  # Blue Rectangle
    pygame.draw.polygon(screen, GREEN, [(150, 250), (250, 250), (200, 150)])  # Green Triangle
    
    pygame.display.flip()
    
    # Event Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

Q4Picture()
