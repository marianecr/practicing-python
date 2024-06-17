'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''

soma = 0
count = 0

for c in range(0, 6):
    numero = int(input('Digite um número inteiro: '))

    if numero % 2 == 0:
        soma += numero
        count += 1

print(f'Foram {count} números pares digitados. A soma deles é igual a {soma}.')