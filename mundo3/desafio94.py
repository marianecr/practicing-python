"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média"""
pessoa = dict()
pessoas_acima_media = dict()
cad_pessoas = list()
total_idade = 0
mulheres = list()
while True:
  pessoa['nome'] = str(input('Nome: ')).strip()
  pessoa['genero'] = str(input('Gênero: ')).strip().upper()

  if pessoa['genero'] == 'F':
    mulheres.append(pessoa['nome'])
  
  while pessoa['genero'] not in 'FMO':
    print('Opção inválida! Digite F para feminino, M para masculino ou O para outros gêneros.')
    pessoa['genero'] = str(input('Gênero: ')).strip().upper()
  
  pessoa['idade'] = int(input('Idade: '))

  resp = str(input('Deseja cadastrar mais alguém? [S/N]: ')).strip().upper()
  while resp not in 'SN':
    print('Opção inválida! Digite S para "Sim" ou N para "Não".')
    resp = str(input('Deseja cadastrar mais alguém? [S/N]: ')).strip().upper()
  
  cad_pessoas.append(pessoa.copy())
  total_idade += pessoa['idade']
  if resp == 'N':
    break
media = total_idade / len(cad_pessoas)

print(f'A) Foram cadastradas {len(cad_pessoas)} pessoas.')
print(f'B) A média de idade do grupo é de {media:.1f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}.')
print(f'D) Pessoas acima da média de idade do grupo:')
for p in cad_pessoas:
  if p['idade'] > media:
    for k, v in p.items():
      print(f'{k} = {v}; ', end='')
  print()
