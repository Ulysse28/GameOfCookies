import pygame

class Spider(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 50
        self.max_health = 100
        self.velocity = 1
        self.image = pygame.image.load('images/spider.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def move_down(self):
        self.rect.y = self.rect.y + self.velocity

    def update_health_bar(self, surface):

        #définir la couleur de la jauge de vie
        bar_color = (111, 210, 46)
        #définir une autre couleur pour la jauge
        back_bar_color = (241, 54, 14)

        #définir la jauge de vie
        bar_position = [self.rect.x - 18, self.rect.y - 7, self.health, 5]
        back_bar_position = [self.rect.x - 18, self.rect.y - 7, self.max_health, 5]


        #déssiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)