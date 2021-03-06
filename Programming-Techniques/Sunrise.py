import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My First Flipbook")

game_over = False
circle_x = -40
circle_y = 230
A = 1

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
            
    # -- Game logic goes after this comment
    ### SRC - I really like this approach, very efficient.
    if circle_x > 700:
        circle_x = -40
    else:
        circle_x += 2
    ### SRC - END IF
    A = 2
    if A == 2:
        if circle_x < 290:
            circle_y -= 1
        else:
            circle_y += 1
        ### SRC - END IF
    ### SRC - END IF

    
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    pygame.draw.rect(screen, BLUE, (220,240,200,150))
    pygame.draw.circle(screen, YELLOW, (circle_x,circle_y),40,0)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
