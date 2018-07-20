"""
title: smiley
author: Nisha Seyed
date: 7/20/18 9:42 AM
"""

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (246, 226, 51)
BROWN = (153, 102, 51)



PI = 3.141592653
x_coord, x_speed, y_coord, y_speed = 0, 0, 0, 0
ball_pos_x, ball_pos_y = 310, 310
ball_speed_x, ball_speed_y = 0, 3


ball_pos = 0

# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Move stick figure")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

def draw_stick_figure(screen, x, y):
    pygame.draw.line(screen, BLACK, [200+ x, 200 + y], [200 + x , 450 + y], 8)
    pygame.draw.line(screen, GREEN, [150 + x, 400 + y], [250 + x, 400 + y], 20)

    pygame.draw.ellipse(screen, YELLOW, [120 + x, 150 + y, 200, 200])
    pygame.draw.ellipse(screen, BLUE, [180 + x, 180 + y, 20, 30])
    pygame.draw.ellipse(screen, BLACK, [230 + x, 170 + y, 50, 50])

    pygame.draw.arc(screen, BLACK, [190 + x, 160 + y, 50, 20], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, BLACK, [200 + x, 350 + y, 70, 20], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, BLACK, [220 + x, 350 + y, 70, 20], PI, 3 * PI / 2, 2)

    pygame.draw.arc(screen, BLACK, [210 + x, 450 + y, 70, 20], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, BLACK, [190 + x, 430 + y, 50, 50], PI, 3 * PI / 2, 2)

    pygame.draw.arc(screen, BLUE, [150 + x, 150 + y, 150, 150], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, RED, [150 + x, 150 + y, 150, 150], 3 * PI / 2, 2 * PI, 2)
    pygame.draw.arc(screen, BLACK, [220 + x, 250 + y, 50, 10], PI, 3 * PI / 2, 2)



def draw_coconut(screen, x, y):
    pygame.draw.circle(screen, BROWN, (x, y), 30)
    pygame.draw.line(screen, BLACK, [10 + x, 15 + y], [30 + x, 20 + y], 5)
    pygame.draw.line(screen, BLACK, [10 + x, 40 + y], [10 + x, 10 + y], 2)



# Loop as long as done == False
while not done:


    if ball_pos_y > (500 + y_coord):
        ball_speed_y = -3
    if ball_pos_y < (400 + y_coord):
        ball_speed_y = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed= -3
            elif event.key == pygame.K_RIGHT:
                x_speed= 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed= 3
        elif event.type == pygame.KEYUP:
            x_speed = 0
            y_speed = 0


    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    ball_pos_y = ball_pos_y + ball_speed_y
    ball_pos_x = x_coord + 270

    draw_stick_figure(screen, x_coord, y_coord)
    draw_coconut(screen, ball_pos_x, ball_pos_y)

    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.

    # # This draws a triangle using the polygon command
    # pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    #text = font.render("My text", True, BLACK)

    # Put the image of the text on the screen at 250x250
    #screen.blit(text, [250, 250])

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
