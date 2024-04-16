'''O mesmo professor do desafio "sorteando estudante" quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle

estudante1 = input('Digite o nome do primeiro estudante: ')
estudante2 = input('Digite o nome do segundo estudante: ')
estudante3 = input('Digite o nome do terceiro estudante: ')
estudante4 = input('Digite o nome do quarto estudante: ')

alunos = [estudante1, estudante2, estudante3, estudante4]

shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')