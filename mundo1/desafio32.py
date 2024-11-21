"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""
from datetime import date

ano = int(input('Digite o ano (para o ano atual, digite 1): '))

if ano == 1:
    ano = date.today().year
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é um bissexto.')