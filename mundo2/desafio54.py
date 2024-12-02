"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date

maiores = 0
menores = 0
ano_atual = date.today().year

for i in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i}ª: '))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'{maiores} já atingiram a maioridade e {menores} ainda são menores.')
