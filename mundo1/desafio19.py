"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

from random import choice

estudante1 = input('Digite o nome do primeiro estudante: ')
estudante2 = input('Digite o nome do segundo estudante: ')
estudante3 = input('Digite o nome do terceiro estudante: ')
estudante4 = input('Digite o nome do quarto estudante: ')

alunos = [estudante1, estudante2, estudante3, estudante4]

print(f'O estudante escolhido foi {choice(alunos)}.')