import pygame
import sys
import random

from pygame.examples.scrap_clipboard import screen


class Ball:
    def __init__(self,screen,color,x,y,radius,speed_x,speed_y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color
        self.radius = radius

    def move(self):

        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen.get_height():
            self.speed_y = -self.speed_y
        if self.x - self.radius <= 0 or self.x + self.radius>= self.screen.get_width():
            self.speed_x = -self.speed_x
        self.x += self.speed_x
        self.y += self.speed_y





    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    # def at_lrborder(self): # L & R
    #     return self.x < 0 or self.x + > self.screen.get_width()
    #
    # def at_udborder(self): # U & D
    #     return self.y < 0 or self.y > self.screen.get_height()










# You will implement this module ENTIRELY ON YOUR OWN!

# TO/DO: Create a Ball class.
# TO/DO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TO/DO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    radius = random.randint(1, 5)
    x = random.randint(0 + radius, screen.get_width() - radius)
    y=  random.randint(0 + radius, screen.get_height() - radius)
    speed_x = random.randint(1, 12)
    speed_y = random.randint(1,12)

    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    # TODO: Create an instance of the Ball class called ball1
    ball1 = Ball(screen,color,x,y,radius,speed_x,speed_y)




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('white'))

        ball1.draw()
        ball1.move()
        # TODO: Move the ball
        # TODO: Draw the ball

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
