import pygame

print("Setup Start") #indiferente somente a fim de testes e depuração
pygame.init()
screen = pygame.display.set_mode(size=(600, 480))
print("Setup End") #indiferente somente a fim de testes e depuração

print("Loop Start") #indiferente somente a fim de testes e depuração
while True:
    for event in pygame.event.get(): #checar por todos os eventos
        if event.type == pygame.QUIT: #se o evento for de fechar a janela
            pygame.quit() #fechar a janela
            quit() #sair do programa
            