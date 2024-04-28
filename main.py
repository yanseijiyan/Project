import pygame 


pygame.init()


# Set the window size
window = pygame.display.set_mode((1280, 720))    
title = pygame.display.set_caption("Game_test")

# Load the background image
field = pygame.image.load("assets/field.png")
window.blit(field, (0, 0))

# Load the player image
player = pygame.image.load("assets/player1.png")
window.blit(player, (85,300))

player2 = pygame.image.load("assets/player2.png")
window.blit(player2, (1100,300))

ball = pygame.image.load("assets/ball.png")
window.blit(ball, (620,330))
#
loop = True
# Main loop
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False    


    pygame.display.update()