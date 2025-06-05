import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    image = pygame.image.load("2dogs.JPG")
    image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))
    # TODO 1: Create an image with the 2dogs.JPG image
    # TODO 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)


    # Prepare the text caption(s)
    # TODO 4: Create a font object with a size 28 font.
    font1 = pygame.font.SysFont("corbel", 28)
    caption1 = font1.render("Two Dogs", True, BLACK)
    # TODO 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).

    # Prepare the music
    # TODO 8: Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("bark.mp3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                    bark_sound.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        screen.blit(image,(0,0))
        # TODO 2: Draw (blit) the image onto the screen at position (0, 0)

        # Draw the text onto the screen
        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        screen.blit(caption1, (screen.get_width() / 2 - caption1.get_width() / 2, image.get_height() - 2))
        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.
        font2 = pygame.font.SysFont("ariel", 50)
        caption2 = font2.render("DIBS!", True, BLACK)
        screen.blit(caption2, (screen.get_width() / 2 - caption2.get_width() / 2, image.get_height() - 100))


        # Update the screen
        pygame.display.update()


main()
