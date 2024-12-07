"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import date
ano_atual = date.today().year
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip()
ano_nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = ano_atual - ano_nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if pessoa['ctps'] != 0:
  pessoa['contratação'] = int(input('Ano de Contratação: '))
  pessoa['salário'] = float(input('Salário: R$'))
  pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - ano_nascimento

print('=' * 35)
for k, v in pessoa.items():
  print(f'-> {k} - {v}')
