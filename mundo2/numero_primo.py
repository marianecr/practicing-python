''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

numero = int(input('Digite um número inteiro qualquer: '))
total = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        total += 1

    else:
        print('\033[34m', end='')

    print(f'{c}', end=' ')

print(f'\nO número {numero} foi divisível {total} vezes.')

if total == 2:
    print('Ele é um número primo.')
else:
    print('Ele não é um número primo.')
