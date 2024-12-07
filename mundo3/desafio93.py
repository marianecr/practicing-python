"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato"""
jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(partidas):
  gols.append(int(input(f'Quantos gols marcados na {p + 1}ª partida? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('=' * 40)
print(jogador)
print('=' * 40)

for k, v in jogador.items():
  print(f'{k} -> {v}')

print('=' * 40)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for i in range(partidas):
  print(f'  => Na {i + 1}ª partida, marcou {jogador["gols"][i]}.')
print(f'Foi um total de {sum(gols)} gols.')