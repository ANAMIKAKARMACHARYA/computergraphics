import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a line using DDA algorithm
def draw_line_bresh(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1
    for i in range(steps):
        screen.set_at((round(x), round(y)), WHITE)
        x += x_increment
        y += y_increment
        print(x,y)
      

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        draw_line_bresh(320, 430,320, 530)
        draw_line_bresh(320,430,420,430)
        draw_line_bresh(420,430,420,530)
        draw_line_bresh(320,530,420,530)
        draw_line_bresh(320,530,370,630)
        draw_line_bresh(370,630,420,530)
        draw_line_bresh(320,430,370,330)
        draw_line_bresh(370,330,420,430)
        draw_line_bresh(320,430,220,480)
        draw_line_bresh(220,480,320,530)
        draw_line_bresh(420,530,520,480)
        draw_line_bresh(520,480,420,430)

        

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
