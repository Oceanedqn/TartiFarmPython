import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.name = "Joueur"
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.skills = {'fishing': 0, 'mining': 0, 'haxing': 0}
        self.image = pygame.image.load('assets/perso.png')
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300


    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def move_right_up(self):
        self.rect.x += self.velocity
        self.rect.y -= self.velocity

    def move_right_down(self):
        self.rect.x += self.velocity
        self.rect.y += self.velocity

    def move_left_up(self):
        self.rect.x -= self.velocity
        self.rect.y -= self.velocity

    def move_left_down(self):
        self.rect.x -= self.velocity
        self.rect.y += self.velocity