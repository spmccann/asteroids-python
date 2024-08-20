import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        pygame.Surface.fill(screen, color="black")
        pygame.display.flip()
        print("Starting asteroids!")
        print("Screen width:", SCREEN_WIDTH) 
        print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
