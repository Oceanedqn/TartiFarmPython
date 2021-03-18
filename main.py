import pygame
import pyautogui
from game import Game
pygame.init()


#width, height = pyautogui.size()
width, height = 1200, 900
pygame.display.set_caption("TartiFarm")
screen = pygame.display.set_mode((width, height))


background = pygame.image.load('assets/background.jpg')
game = Game()


running = True

#Boucle du jeu
while running:
    #appliquer arriere plan
    screen.blit(background, (0,0))

    #appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    #verifier si le joueur souhaite bouger



    if game.pressed.get(pygame.K_q) and game.pressed.get(pygame.K_z):
        game.player.move_left_up()
    elif game.pressed.get(pygame.K_q) and game.pressed.get(pygame.K_s):
        game.player.move_left_down()
    elif game.pressed.get(pygame.K_d) and game.pressed.get(pygame.K_z):
        game.player.move_right_up()
    elif game.pressed.get(pygame.K_d) and game.pressed.get(pygame.K_s):
        game.player.move_right_down()
    elif game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < width:
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_z):
        game.player.move_up()
    elif game.pressed.get(pygame.K_s):
        game.player.move_down()



    #mettre à jour l'écran
    pygame.display.flip()

    # Sortir du jeu
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            running = False
            pygame.quit()
            print("Fermeture du jeu")


        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False




