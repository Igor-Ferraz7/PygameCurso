import pygame
from rr import Ship

display = pygame.display.set_mode([480, 1000]) #[683, 384]
pygame.display.set_caption('Meu primeiro jogo :)')

conjuto = pygame.sprite.Group()
eye = pygame.sprite.Sprite(conjuto)
eye.image = pygame.image.load("data\Olhinho.png")
eye.rect = pygame.Rect([400, 250, 100, 100])
eye.image = pygame.transform.scale(eye.image, [100, 100])

bucket = pygame.sprite.Sprite(conjuto)
bucket.image = pygame.image.load('data\Baldinho.png')
bucket.image = pygame.transform.scale(bucket.image, [100, 100])
bucket.rect = pygame.Rect([400, 250, 100, 100])

pygame.mixer.init()
pygame.mixer.music.load('data\song18.mp3')
pygame.mixer.music.play(-1)
fb = pygame.mixer.Sound('data//fireball.wav')


cubo = pygame.Rect([50, 50, 100, 100])
gameloop = True
if __name__ == '__main__':
    while gameloop:
        keys = pygame.key.get_pressed()
        display.fill([46, 46, 46])
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                gameloop = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_f:
                    fb.play()
        if keys[pygame.K_w]:
            eye.rect.y -= 1
            bucket.rect.x += 1
        elif keys[pygame.K_s]:
            eye.rect.y += 1
            bucket.rect.x -= 1
        pygame.draw.rect(display, [35, 250, 2], cubo)
        conjuto.draw(display)
        pygame.display.update()
