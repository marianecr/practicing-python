"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 18:
    tempo_restante = 18 - idade
    print(f'Você tem apenas {idade} anos. Ainda não está na hora de se alistar. Faltam {tempo_restante} anos. Seu alistamento será em {anoAtual + tempo_restante}.')
elif idade == 18:
    print('Está na hora de se alistar.')
else:
    tempo_excedido = idade - 18
    print(f'Você tem {idade} anos. Já se passaram {tempo_excedido} anos do prazo de alistamento. Seu alistamento era em {anoAtual - tempo_excedido}.')