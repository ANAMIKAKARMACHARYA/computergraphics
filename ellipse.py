import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid point ellipse Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw an ellipse using the Midpoint Ellipse Algorithm
def draw_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = (ry**2) - (rx**2 * ry) + (0.25 * rx**2)
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y
    # First region (ellipse with greater y-radius)
    while dx < dy:
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        screen.set_at((xc + x, yc - y), WHITE)
        screen.set_at((xc - x, yc - y), WHITE)

        if p1 < 0:
            x += 1
            dx = 2 * ry**2 * x
            p1 += dx + ry**2
        else:
            x += 1
            y -= 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            p1 += dx - dy + ry**2

    # Second region (ellipse with greater x-radius)
    p2 = (ry**2) * (x + 0.5)**2 + (rx**2) * (y - 1)**2 - (rx**2) * (ry**2)
    
    while y >= 0:
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        screen.set_at((xc + x, yc - y), WHITE)
        screen.set_at((xc - x, yc - y), WHITE)

        if p2 > 0:
            y -= 1
            dy = 2 * rx**2 * y
            p2 += rx**2 - dy
        else:
            x += 1
            y -= 1
            dx = 2 * ry**2 * x
            dy = 2 * rx**2 * y
            p2 += dx - dy + rx**2

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw the ellipse (center, rx, ry)
        draw_ellipse(400, 400, 300, 150)
      

        # Update the display
        pygame.display.flip()

# Run the main loop
if __name__ == "__main__":
    main()
