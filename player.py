import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.personnage = pygame.image.load('mario..png')
        self.personnage = pygame.transform.scale(self.personnage, (100, 100))
        self.image = self.get_image(0, 0)
        # Vitesse du déplacement
        self.speed = 50
        #Position du personnage en x et en y
        self.x = x
        self.y = y
        #Attributs sauter
        self.saut = 0
        self.saut_descente = 0.5
        self.saut_montee = 0
        self.a_sauter = False
        # Vitesse du personnage
        self.clock = pygame.time.Clock()

        # position initiale du player
        self.rect = self.image.get_rect()

        self.collision_sol = [0, 400]

    def update(self):
        self.rect.topleft = self.x, self.y

    def get_image(self, x, y):
        # Je découpe l'image sur des coordonnées précisées en x et y
        image = pygame.Surface([32, 32])
        # image.blit((self.sprite_sheet, (0, 0), (x, y, 32, 32)))
        return image

    def sauter(self):
        self.a_sauter = True
        if self.a_sauter:
            if self.saut_montee >= 0.10:
                self.saut_descente -= 0.1
                self.saut = self.saut_descente
            else:
                self.saut_montee += 0.1
                self.saut = self.saut_descente

            if self.saut_descente < 0:
                self.saut_montee = 0
                self.saut_descente = 0.5
                self.a_sauter = False

        #self.y -= (10 * (self.saut / 2))
        self.y -= 2







