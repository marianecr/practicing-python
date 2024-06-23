'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
from time import sleep

print('=' * 60)
print('VOU PENSAR EM UM NÚMERO DE 0 ATÉ 10. TENTE ADIVINHAR QUAL.')
print('=' * 60)
sleep(3)

num_PC = randint(0, 10)
palpite = int(input('Pensei! Qual você acha que foi? '))
tentativas = 1

while palpite != num_PC:
    palpite = int(input('Não foi esse não. Tenta outra vez: '))
    tentativas += 1

if tentativas == 1:
    print(f'VOCÊ ACERTOU DE PRIMEIRA. PARABÉNS!🎉.')
else:
    print(f'DEPOIS DE {tentativas} TENTATIVAS, VOCÊ ACERTOU. PARABÉNS!🎉.')