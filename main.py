import pygame as pg
from time import sleep


pg.init()
x= 1024
y= 768
janela = pg.display.set_mode([x, y])
pg.display.set_caption('Meu jogo')

centro_x = int(x/2)
centro_y = int(y/2)
bolinha_x = int(x/2)
bolinha_y = int(y/2)
velocidade = 1


def desenhar():
    janela.fill([19, 173, 235])
    circulo = pg.draw.circle(janela, [0, 0, 0], [bolinha_x, bolinha_y], 10)
    chao = pg.draw.rect(janela, [80, 107, 47], [0, centro_x+10, 1024, centro_y+10])


while True:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.QUIT()
    if keys[pg.K_UP]:
        for pulo in range (0, 4):
            bolinha_y -= velocidade
            sleep(0.0005)
    if keys[pg.K_LALT] and keys[pg.K_F4]:
        pg.QUIT()
    
    if bolinha_y < centro_x:
        bolinha_y += velocidade
        sleep(0.0005)
    desenhar()
    pg.display.update()
