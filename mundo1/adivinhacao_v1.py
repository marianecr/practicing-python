'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep

numero_PC = randint(0, 5)
numero_user = int(input('Digite um número inteiro de 0 a 5: '))

print('Vamos ver...')
sleep(2)

if numero_user == numero_PC:
    print(f'Era o número {numero_PC} mesmo. Você acertou. PARABÉNS!')
else:
    print(f'Você errou! Era o número {numero_PC}. Tente novamente.')