#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from code import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

def run(self):
    while True:
        menu = Menu(self.window)  
        menu.run() 
        pass

        # for event in pygame.event.get(): #checar por todos os eventos
            #     if event.type == pygame.QUIT: #se o evento for de fechar a janela
            #          pygame.quit() #fechar a janela
            #         quit() #sair do programa
