"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""
from random import randint
from time import sleep

def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1,10))

    print(f'Sorteando os valores: ', end='')
    for n in numeros:
        print(n, end=' ')
        sleep(0.8)
    print('SORTEADO!')


def soma_pares(lis):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'O total da soma dos valores pares de {numeros} é {soma}.')


# Programa principal
numeros = []
sorteia()
soma_pares(numeros)