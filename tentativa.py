#fazer um programa
import pygame
from pygame.locals import *
from sys import exit




pygame.init()

largura = 650
altura = 490

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('C C N  PROGRAMAS')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255, 0, 0), (200, 300, 30, 30))
    pygame.draw.rect(tela, (0, 0, 255,), (250, 300, 30, 30))
    pygame.draw.rect(tela, (0, 255, 0,), (150, 300, 30, 30))
    pygame.draw.rect(tela, (150, 0, 0,), (100, 300, 30, 30))
    pygame.draw.rect(tela, (0, 125, 123,), (50, 300, 30, 30))
    pygame.draw.rect(tela, (255, 125, 123,), (300, 300, 30, 30))
    pygame.draw.rect(tela, (255, 255, 123,), (350, 300, 30, 30))
    pygame.draw.rect(tela, (255, 0, 123,), (400, 300, 30, 30))
    pygame.draw.rect(tela, (1, 100, 50,), (400, 300, 30, 30))
    pygame.draw.rect(tela, (100, 100, 0,), (450, 300, 30, 30))
    pygame.draw.rect(tela, (75, 75, 75,), (500, 300, 30, 30))
    pygame.draw.rect(tela, (255, 255, 255,), (550, 300, 30, 30))
    pygame.draw.circle(tela, (255, 255, 0), (325, 50), 40)
    pygame.draw.line(tela, (255, 0, 0), (240, 100), (400, 100), 5)

    pygame.display.update()