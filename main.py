# Instantation de la classe pygame
import pygame
from game import Game

if __name__ == '__main__':
    pygame.init()
#Instantation d'un objet Game
    game = Game()
#Appel de la fonction principale qui démarre le jeu (boucle)
    game.run()
    # Quitter le jeu
    pygame.quit()
