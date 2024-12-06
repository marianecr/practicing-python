"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""
numeros = []
pares = []
impares = []
for i in range(1, 8):
  num = int(input(f'Digite o {i}º número: '))

  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)
  
numeros.append(pares[:])
numeros.append(impares[:])
pares.sort()
impares.sort()
print(f'Os valores digitados foram: {numeros}.')
print(f'Pares: {pares}.')
print(f'Ímpares: {impares}.')
