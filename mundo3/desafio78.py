"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""
numeros = []
for i in range(1,6):
  num = int(input(f'Digite o {i}º número: '))
  numeros.append(num)
print(f'Os valores digitados foram: {numeros}.')
print(f'O maior valor foi {max(numeros)} e o menor foi {min(numeros)}.')
