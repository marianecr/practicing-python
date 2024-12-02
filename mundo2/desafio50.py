"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""
soma = 0
count = 0

for i in range(1,7):
    num = int(input(f'Digite o {i}° número: '))
    if num % 2 == 0:
        soma += num
        count += 1
print(f'Foram digitados {count} números pares e a soma deles é igual a {soma}.')