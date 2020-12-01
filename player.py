import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):


    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 500
        self.velocity = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('werewolf.png')
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

    def move_right(self):
        #si le joueur n'est pas en collision avec un enemy


        self.rect.x = self.rect.x + self.velocity

    def move_left(self):
        # si le joueur n'est pas en collision avec un enemy
        self.rect.x = self.rect.x - self.velocity

    def move_up(self):
        # si le joueur n'est pas en collision avec un skull
        if not self.game.check_collision(self, self.game.all_skulls):
            self.rect.y = self.rect.y - self.velocity
        #if not self.game.check_collision(self, self.game.all_spiders):
            #self.rect.y = self.rect.y - self.velocity

    def update_health_bar(self, surface):

        #déssiner la barre de vie
        pygame.draw.rect(surface, (241, 54, 14), [self.rect.x - 18, self.rect.y - 7, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 18, self.rect.y - 7, self.health, 5])

    def move_down(self):
        # si le joueur n'est pas en collision avec un enemy
        self.rect.y = self.rect.y + self.velocity

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self, self))


    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount



