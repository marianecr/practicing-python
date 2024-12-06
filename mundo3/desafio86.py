"""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta."""
matriz = [[], [], []]
for l in range(0, 3):
  for v in range(0, 3):
    num = int(input(f'Digite um valor para {l, v}: '))
    matriz[l].append(num)

for i in matriz:
    print(f'[ {i[0]:^3} ] [ {i[1]:^3} ] [ {i[2]:^3} ]')