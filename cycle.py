import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1000, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BICYCLE")

# Colors
WHITE = (50, 250, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREY = (169, 169, 169)
BLUE = (0, 0, 255)
BROWN = (101, 67, 33)

# Main loop
def main():
    clock = pygame.time.Clock()
    i = 0  
   
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        
        pygame.draw.line(screen,BROWN,(-300, 600),(1000, 600), 30)  
        pygame.draw.circle(screen,GREY,(100+i,550),50)  
        pygame.draw.circle(screen,GREY,(300+i,550),50)  
        pygame.draw.circle(screen,GREY,(190+i,550),25) 
        pygame.draw.line(screen,BLUE,(190+i,550),(125+i,420),5)
        pygame.draw.line(screen,BLUE,(100+i,550),(190+i,550),5)  
        pygame.draw.line(screen,BLUE,(300+i,550),(250+i,350),5)  
        pygame.draw.line(screen,BLUE,(250+i,350),(100+i,550),5)  
        pygame.draw.line(screen,BLUE,(190+i,550),(275+i,440),5)
        pygame.draw.ellipse(screen,BROWN,(110+i,415,55,25))  
        pygame.draw.line(screen,BROWN,(200+i,300),(300+i,400),5)  

        # Update the display
        pygame.display.flip()

        # Increment 
        i=i+2
        if i>WIDTH:  
            i=-300  

        # Limit the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()