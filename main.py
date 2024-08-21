import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable) 
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT /2) 

    AsteroidField.containers = updateable
    Asteroid.containers = (updateable, drawable, asteroids)
    Shot.containers = (shots, updateable, drawable)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        for obj in updateable:
            obj.update(dt)

        pygame.Surface.fill(screen, color="black")

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit() 
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        dt = clock.tick(60)  / 1000

if __name__ == "__main__":
    main()


