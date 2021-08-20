import pygame
# RECT ==>>> POSIÇÃO E FORMATO NO PLANO CARTESIANO
# DISPLAY ==>> TELA
# DRAW ==>> IMPIMIR POR DEFINITIVO NO DISPLAY
# event.get() ==> LISTA TODOS OS EVENTOS QUE ACONTECERÃO
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption('Meu Primeiro Jogo :)')
gameloop = True


def draw():
    display.fill([46, 46, 46])


drawGroup = pygame.sprite.Group()
guy = pygame.sprite.Sprite(drawGroup)
guy.image = pygame.image.load('data\Olhinho.png')
guy.rect = pygame.Rect(50, 50, 100, 100)
guy.image = pygame.transform.scale(guy.image, [100, 100])
# print('Você está pressionando a tecla "w"!!')  # --> fora de conjunto com a do KEYDOWN
player = pygame.Rect(50, 50, 100, 100)
if __name__ == '__main__':
    while gameloop:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                gameloop = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    print('Você pressionou a tecla "w"!')
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_w:
                    print('Você soltou o "w"!')
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:#Probleminha! Tente fazer com que esta condição acione -->
            guy.rect.x += 1
        elif keys[pygame.K_a]:
            guy.rect.x -= 1
        elif keys[pygame.K_w]:
            guy.rect.y -= 1
        elif keys[pygame.K_s]:
            guy.rect.y += 1
        # defina a cor da tela primeiro
        draw()
        #                tela   , cor        , objeto
        pygame.draw.rect(display, [252, 3, 3], player)
        drawGroup.draw(display)
        pygame.display.update()

