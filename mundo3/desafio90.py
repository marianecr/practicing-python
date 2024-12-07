"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
1) Média abaixo de 5 - REPROVADO
2) Entre 5 e 6.9 - Recuperação
3) Acima de 7 - APROVADO"""
estudante = dict()
estudante['nome'] = str(input('Nome: ')).strip()
estudante['média'] = float(input(f'Média de {estudante["nome"]}: '))
if estudante['média'] < 5:
  estudante['Situação'] = 'Reprovado'
elif estudante['média'] > 7:
  estudante['Situação'] = 'Aprovado'
else:
  estudante['Situação'] = 'Recuperação'

print('=' * 30)
for k, v in estudante.items():
  print(f'{k} é igual a {v}.')