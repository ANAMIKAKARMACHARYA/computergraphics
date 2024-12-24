import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bersenham's Line Drawing Algorithm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_line_dda(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x2 > x1:
        lx = 1
    else:
        lx = -1
    if y2 > y1:
        ly = 1
    else:
        ly = -1
    x = x1
    y = y1
    if dx > dy:
        p = 2 * dy - dx
        screen.set_at((round(x), round(y)), WHITE)  
        while not (x == x2):
            if p < 0:
                x = x + lx
                y = y
                p = p + 2 * dy
            else:
                x = x + lx
                y = y + ly
                p = p + 2 * dy - 2 * dx
            screen.set_at((round(x), round(y)), WHITE)  
    else:
        p = 2 * dx - dy
        screen.set_at((round(x), round(y)), WHITE)  
        while not (y == y2):
            if p < 0:
                x = x
                y = y + ly
                p = p + 2 * dx
            else:
                x = x + lx
                y = y + ly
                p = p + 2 * dx - 2 * dy
            screen.set_at((round(x), round(y)), WHITE)  

def main():
    while True:  # Change: Use 'True' instead of 'TRUE'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK) 

        draw_line_dda(200, 400, 200, 440)
        draw_line_dda(200, 440, 280, 440)
        draw_line_dda(200, 400, 280, 400)
        draw_line_dda(280, 400, 280, 440)
        pygame.display.flip()

if __name__ == "__main__":
    main()