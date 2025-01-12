import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Translation")

# Colors
WHITE = (50, 250, 255)
BLACK = (0, 0, 0)

# Function to draw a line using the Midpoint Line Algorithm
def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)
    xinc = dx / step
    yinc = dy / step
    x = x1
    y = y1
    for i in range(step):
        screen.set_at((round(x), round(y)), WHITE)
        x=x+xinc
        y=y+yinc

# Main loop
def main():
    x1, y1 = 200, 400
    x2, y2 = 400, 300 
    tx, ty = 50, 50  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)
        draw_line(x1, y1, x2, y2)
        draw_line(x1 + tx, y1 + ty, x2 + tx, y2 + ty)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()