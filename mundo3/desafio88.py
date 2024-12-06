"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep

print('=' * 40)
print(f'{'MEGA SENA':^40}')
print('=' * 40)
qtde_jogos = int(input('Quantos jogos deseja fazer? '))
print('=' * 40)
print(f'{f" SORTEANDO {qtde_jogos} JOGOS ":*^40}')

temporaria = []
jogos = []

for j in range(qtde_jogos):
  while True:  
    num = randint(1, 60)
    if num not in temporaria:
      temporaria.append(num)
    if len(temporaria) >= 6:
      break
      
  temporaria.sort()
  jogos.append(temporaria[:])
  temporaria.clear()

  print(f'Jogo {j + 1}: {jogos[j]}')
  sleep(1)
