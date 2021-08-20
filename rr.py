import pygame, math

class Ship(pygame.sprite.Sprite):
    def __init__(self, *groups, local):
        super().__init__(*groups)  # O SUPER() É USADO PARA O __INIT__ CRIADO (OBJETOS) NÃO SOBREPOR O __INIT__ HERDADO (SPRITE)
        self.image = pygame.image.load(local)
        self.fb = pygame.mixer.Sound('data//fireball.wav')
        self.rect = pygame.Rect([400, 250, 200, 200])
        self.image = pygame.transform.scale(self.image, [200, 200])
        self.speed = 0
        self.acel = 0.1

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 680:
            self.rect.bottom = 680

        if keys[pygame.K_d]:
            self.rect.x += 1
        if keys[pygame.K_a]:
            self.rect.x -= 1
        if keys[pygame.K_w]:
            self.rect.y -= 1

            self.speed -= self.acel
        if keys[pygame.K_s]:
            self.rect.y += 1
            self.speed += self.acel
        else:
            self.speed *= 0.95

        self.rect.y += self.speed
class Bot(pygame.sprite.Sprite):
    def __init__(self, *groups, local):
        super().__init__(*groups)
        self.image = pygame.image.load(local)
        self.rect = pygame.Rect([400, 250, 100, 100])
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.timer = 0

    def update(self, *args, **kwargs):
        self.timer += 0.001
        self.rect.y = 250 + math.sin(self.timer) * 200
