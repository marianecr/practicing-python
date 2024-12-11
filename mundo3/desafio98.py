"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, a cada 1
b) de 10 até 0, a cada 2
c) uma contagem personalizada"""
from time import sleep
def print_linha():
    print('=' * 30)


def contagem(inicio, fim, passo):
    print_linha()
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}.')

    if fim < inicio:
        fim -= 1
        if not passo <= 0:
            passo *= -1
    if fim <= 0:
        fim += -1
    if fim > 0 and inicio < fim:
       fim += 1

    for n in range(inicio, fim, passo):
        print(n, end=' ')
        sleep(0.5)
    print('FIM!')


# Programa principal
contagem(1, 10, 1)
contagem(10, 0, 2)
print_linha()
print('Agora personalize sua contagem!')
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))