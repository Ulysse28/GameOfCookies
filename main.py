import pygame
from game import Game



pygame.init()



#classe qui représente le joueur:

#générer la première fenetre

pygame.display.set_caption("MyGame")
screen = pygame.display.set_mode((1080, 600))

background = pygame.image.load('imageFond.jpg')

#charger le jeu
game = Game()

running = True



while running:


    #appliquer l'arrière plan du jeu
    screen.blit(background, (0, 0))



    #appliquer l'image du joueur:

    screen.blit(game.player.image, game.player.rect)
    game.player.update_health_bar(screen)

    #récuperer les projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()

    game.player.all_projectiles.draw(screen)

    #appliquer l'image d'un skull

    game.all_skulls.draw(screen)

    #appliquer l'image du spider
    game.all_spiders.draw(screen)

    #déplacement du skull
    for skull in game.all_skulls:
        skull.update_health_bar(screen)
        skull.move_down()
        #skull.launch_projectile()


    #déplacement du spider
    for spider in game.all_spiders:
        spider.update_health_bar(screen)
        spider.move_down()


    #vérifier si le joueur va à gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 1020:
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < 520:
        game.player.move_down()





    print(game.player.rect.x)

    #mettre à jour l'écran
    pygame.display.flip()


    #si je joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False





