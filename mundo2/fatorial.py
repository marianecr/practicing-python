'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

numero = int(input('Digite um número: '))
fatorial = 1
c = numero

while c > 0:
    fatorial *= c
    c -= 1

print(f'{numero}! é {fatorial}.')