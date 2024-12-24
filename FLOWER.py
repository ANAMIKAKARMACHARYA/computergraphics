import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid point circle Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0,0, 0)

# Function to draw a line using DDA algorithm
def draw_circle(xc,yc,r):
    x=0
    y=r
    p=1-r
    screen.set_at((xc+y,yc+x),WHITE)
    while  x<=y:
        x=x+1
        if p<0:
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*x-2*y+1
        screen.set_at((xc+y,yc+x),WHITE)
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc+y,yc-x),WHITE)
        screen.set_at((xc-y,yc+x),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc-y,yc-x),WHITE)
def draw_petals(xc,yc,r):
    x=0
    y=r
    p=1-r
    screen.set_at((xc+y,yc+x),WHITE)
    while  x<=y:
        x=x+1
        if p<0:
            p=p+2*x+1
        else:
            y=y-1
            p=p+2*x-2*y+1
        screen.set_at((xc+y,yc+x),WHITE)
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc+y,yc-x),WHITE)
        screen.set_at((xc-y,yc+x),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc-y,yc-x),WHITE)
 

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)
        # draw a circle
        # center point
        draw_circle(250,250,50)
        #petals
        draw_petals(200,165,50)
        draw_petals(350,250,50)
        draw_petals(200,335,50)
        draw_petals(150,250,50)
        draw_petals(300,165,50)
        draw_petals(300,335,50)
      

        pygame.display.flip()

if __name__ == "__main__":
    main()
   
   





