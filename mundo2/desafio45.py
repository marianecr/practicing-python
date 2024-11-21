"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import choice
from time import sleep

jogada = int(input('''Faça sua escolha
1 - PEDRA
2 - PAPEL
3 - TESOURA
>>> '''))

if jogada == 1 or jogada == 2 or jogada == 3:
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    opcao_PC = choice(opcoes)

    if jogada == 1:
        opcao_user = 'PEDRA'
    elif jogada == 2:
        opcao_user = 'PAPEL'
    elif jogada == 3:
        opcao_user = 'TESOURA'

    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOOURA')
    sleep(1)    
    
    print('=' * 16)
    print(f'JOGADOR: {opcao_user}')
    print(f'PC: {opcao_PC}')
    print('=' * 16)

    if opcao_user == 'PEDRA':
        if opcao_PC == 'PAPEL':
            print('PC GANHOU!')
        elif opcao_PC == 'TESOURA':
            print('JOGADOR GANHOU!')
        else:
            print('EMPATE!')
    
    elif opcao_user == 'PAPEL':
        if opcao_PC == 'PAPEL':
            print('EMPATE!')
        elif opcao_PC == 'PEDRA':
            print('JOGADOR GANHOU!')
        else:
            print('PC GANHOU!')
    
    else:
        if opcao_PC == 'PAPEL':
            print('JOGADOR GANHOU!')
        elif opcao_PC == 'PEDRA':
            print('PC GANHOU!')
        else:
            print('EMPATE!')

else:
    print('Jogador fez uma opção de jogada inválida. Tente novamente.')
