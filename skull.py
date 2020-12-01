import pygame
import random
from projectile import Projectile

class Skull(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.game = game
        self.velocity = 1
        self.image = pygame.image.load('images/skull.png')
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1080)
        self.rect.y = 10

    def update_health_bar(self, surface):

        #déssiner la barre de vie
        pygame.draw.rect(surface, (241, 54, 14),[self.rect.x - 18, self.rect.y - 7, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 18, self.rect.y - 7, self.health, 5])


    def move_down(self):

        if self.rect.y > 600:
            self.rect.y = self.rect.y = random.randint(0, 1080)
        #si il n'y a pas de  avec le joueur colision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y = self.rect.y + self.velocity
        else:
            self.game.player.damage(self.attack)




    #infliger les dégats

    def damage(self, amount):
        self.health -= amount

        #vérifier si le skull a encore de la vie

        if self.health <= 0:
            self.rect.y = random.randint(0, 1080)
            self.health = self.max_health

   # def launch_projectile(self):
       # self.all_projectiles.add(Projectile(self, self))

