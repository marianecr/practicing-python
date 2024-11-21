"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep

print('='* 19)
print('JOGO DE ADIVINHAÇÃO')
print('='* 19)
print('Pensarei em um número de 0 a 5.')
print('Vamos ver...')

numero_PC = randint(0, 5)
sleep(2)
numero_user = int(input('Pronto! Tente adivinhar o número entre 0 e 5 que pensei: '))

if numero_user == numero_PC:
    print(f'Era o número {numero_PC} mesmo. Você acertou. PARABÉNS!')
else:
    print(f'Você errou! Era o número {numero_PC}. Tente novamente.')