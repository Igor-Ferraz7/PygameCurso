import pygame
from rr import Ship, Bot
display = pygame.display.set_mode([480, 680])
pygame.display.set_caption('Meu primeiro jogo :)')

ator_group = pygame.sprite.Group()

pygame.mixer.init()
pygame.mixer.music.load('data//musica.wav')
pygame.mixer.music.play(-1)
fb = pygame.mixer.Sound('data//fireball.wav')

bg = pygame.sprite.Sprite(ator_group)
bg.image = pygame.image.load('data//PSpace.png')
bg.image = pygame.transform.scale(bg.image, [480, 680])
bg.rect = bg.image.get_rect()

clock = pygame.time.Clock()

gameloop = True

Nave = Ship(ator_group, local="data//NAVE1.png")
Bucket1 = Bot(ator_group, local="data//Baldinho.png") #CTRL X APAGA LINHA
Bucket1.rect.center = [200, 250]
if __name__ == '__main__':
    while gameloop:
        clock.tick(60)
        display.fill([46, 46, 46])
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                gameloop = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_f:
                    fb.play()
        ator_group.update()
        # Bucket.update()
        ator_group.draw(display)
        pygame.display.update()
