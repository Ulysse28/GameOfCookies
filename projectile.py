import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, game):
        super().__init__()
        self.game = game
        self.player = player
        self.velocity = 3
        self.image = pygame.image.load('cookie.png')
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 50
        self.rect.y = player.rect.y + 20

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):

    #si le projectile n'est pas en contact avec un skull
        self.rect.y = self.rect.y - self.velocity
    #si le projectile est en contact
        for skull in self.player.game.check_collision(self, self.player.game.all_skulls):
            self.remove()
            skull.damage(10)
        #for spiders in self.player.game.check_collision(self, self.player.game.all_spiders):
            #self.remove()




        #vérifier si le projectile n'est plus dans l'écran
        if self.rect.y < 0:
            #supprimer le projectile:
            self.remove()
            print("le projectile est supprimé")





