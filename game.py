import pygame

from player import Player


class Game:
    def __init__(self):
        # Taille de l'écran stocké dans une variable screer
        self.screen = pygame.display.set_mode((1024, 768))   # ,  FULLSCREEN)

        # Titre de la fenêtre
        pygame.display.set_caption("My game" )

        # generer un joueur et le positionner sur des coordonnées en paramétre
        self.player = Player(0, 500)
        #Récupération de l'image du joeur
        self.personnage = self.player.personnage
        # Score du joueur
        self.score = 0
        #Vitesse du jeu

    def run(self):
        # Boucle du jeu
        running = True

        while running:
            self.player.x += 0.1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Si l'utilisateur appuye sur un touche
            pressed = pygame.key.get_pressed()
            # Si l'utilisateur appuye sur espace pour sauter alors
            if pressed[pygame.K_SPACE]:
                self.player.sauter()

            # Donne du noir à la place précédente de l'image (Personnage) afin de ne pas avoir la continuité de la
            # trajectoire
            self.screen.fill((255, 255, 255))

            # Affichage du personnage au debut du jeu en fonction des coordonnées x et y
            self.screen.blit(self.personnage, (self.player.x, self.player.y))

            # Met à jour les informations de l'écran en applicant les changements faits
            pygame.display.flip()

            """pygame.display.update((0, 0, 150, 150)) même chose que la méthode précédente sauf qu'il est possible de définir
            où on veut que le changement soit fait // Utile pour faire un random.randint des coordonnés des pièges"""

