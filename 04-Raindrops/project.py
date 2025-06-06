import pygame
import sys
import time
from hero_module import Hero
from cloud_module import Cloud
from raindrop_module import Raindrop


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()

    mike = Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    alyssa = Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")

    cloud = Cloud(screen, 300, 50, "another_cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
                cloud.y -= 10
        if pressed_keys[pygame.K_a]:
            cloud.x -= 10
        if pressed_keys[pygame.K_s]:
                cloud.y += 10
        if pressed_keys[pygame.K_d]:
                    cloud.x += 10

        screen.fill(pygame.Color("white"))

        cloud.draw()


        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        mike.draw()
        alyssa.draw()

        pygame.display.update()




main()