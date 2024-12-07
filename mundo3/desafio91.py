"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
jogadores = dict()
c = 0
for i in range(1, 5):
  jogadores[f'jogador{i}'] = randint(1, 6)

print('VALORES SORTEADOS:')
for k, v in jogadores.items():
  print(f'{k} tirou o valor {v} no dado.')
  sleep(1)
print('=' * 35)
jogadores_ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

print(' === RANKING DOS JOGADORES ===')
while c < 4:
    for k, v in jogadores_ordenado.items():
      print(f'   {c + 1}º Lugar: {k} com {v}.')
      c += 1
      sleep(1)