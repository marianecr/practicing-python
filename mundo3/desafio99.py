"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
from time import sleep
def print_linha():
    print('=' * 30)


def maior_valor(*num):
    print_linha()
    print('Analisando os valores...')
    sleep(1.5)

    if len(num) == 0:
        print('Foram informados 0 valores.')
        print('O maior valor informado foi 0.')

    else:
        for n in num:
            print(n, end=' ')
        print(f'Foram informados {len(num)} valores.')
        print(f'O maior valor foi {max(num)}.')

# Programa principal
maior_valor(1,2,8,25,33,28,96)
maior_valor(87,36,2,9)
maior_valor(5,6,48,21,18,25,3,20,35,69,105,202)
maior_valor()