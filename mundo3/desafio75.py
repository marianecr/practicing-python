"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

numeros = (int(input('Digite o primeiro número:')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

print(f'O número 9 apareceu {numeros.count(9)} vezes.')

if 3 in numeros:
  print(f'O número 3 apareceu primeiro na {numeros.index(3) + 1}ª posição.')
else:
  print('O número 3 não foi digitado nenhuma vez.')

print(f'Os números pares foram: ', end='')

for num in numeros:
  if num % 2 == 0:
    print(num, end=' ')
