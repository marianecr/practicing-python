"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
1) Quantos números foram digitados
2) A lista de valores, ordenada de forma descrecente
3) Se o valor 5 está ou não na lista """
numeros = []
while True:
  num = int(input('Digite um número: '))
  numeros.append(num)
  resposta = str(input('Deseja inserir mais um número [S/N]? ')).strip().upper()
  if resposta == 'N':
    break
print(f'Foram digitados {len(numeros)} valores.')
numeros.sort()
numeros.reverse()
print(f'Lista em ordem descrecente: {numeros}')
if 5 in numeros:
  print(f'O número 5 está na lista e aparece {numeros.count(5)} vezes.')
else:
  print('O número 5 não está na lista.')