import pygame
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# assigning values to X and Y variable
X = 500
Y = 700

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y ))

# set the pygame window name
pygame.display.set_caption('Image')

# create a surface object, image is drawn on it.
image = pygame.image.load('spiral.jpg') #r'/Users/calebdittmar/Documents/Summer\ 2020/Private\ Tutoring/spiral.jpg')

# infinite loop
while True:

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
    display_surface.blit(image, (0, 0))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.

    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        '''
        if event.type == pygame.QUIT :

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()
            '''
        display_surface.blit(image, (80, 80))    
        # Draws the surface object to the screen.
        pygame.display.update()
