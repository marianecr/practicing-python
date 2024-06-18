'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date

anoAtual = date.today().year
menor_total = 0
maior_total = 0

for c in range(0, 7):
    anoDeNascimento = int(input('Digite o ano de nascimento da pessoa: '))
    idade = anoAtual - anoDeNascimento

    if idade >= 18:
        maior_total += 1
    else:
        menor_total += 1

print(f'Há {maior_total} pessoas maiores de idade e {menor_total} pessoinhas que ainda não chegaram aos 18 anos.')
