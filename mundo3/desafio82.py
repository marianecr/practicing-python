"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas."""
numeros = []
pares = []
impares = []
while True:
  num = int(input('Digite um número: '))
  numeros.append(num)
  resposta = str(input('Deseja inserir mais um valor [S/N]? ')).strip().upper()
  if resposta == 'N':
    break

for n in numeros:
  if n % 2 == 0:
    pares.append(n)
  else:
    impares.append(n)

print('=' * 40)
print(f'Os valores digitados foram: {numeros}.')
print(f'Pares: {pares}.')
print(f'Ímpares: {impares}.')
