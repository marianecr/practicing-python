"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""
num = int(input('Digite um número para saber se ele é primo ou não: '))
total = 0

for i in range(1, num + 1):
    if num % i == 0: # Para saber se o número é divisível
        total += 1
print(f'{num} foi divisível {total} vezes.')
if total == 2:
    print(f'Portanto, {num} é um número primo!')
else:
    print(f'Portanto, {num} não é um número primo!')
