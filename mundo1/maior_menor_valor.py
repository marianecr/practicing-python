'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

# Verificando o maior valor
if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior valor.')
if num2 > num1 and num2 > num3:
    print(f'{num2} é o maior valor.')
if num3 > num1 and num3 > num2:
    print(f'{num3} é o maior valor.')

# Verificando o menor valor
if num1 < num2 and num1 < num3:
    print(f'{num1} é o menor valor.')
if num2 < num1 and num2 < num3:
    print(f'{num2} é o menor valor.')
if num3 < num1 and num3 < num2:
    print(f'{num3} é o menor valor.')