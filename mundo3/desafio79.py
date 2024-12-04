"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""
numeros = []
while True:
  num = int(input('Digite um número: '))
  if num not in numeros:
    numeros.append(num)
    print('Número gravado com sucesso!')
  else:
    print('Esse número já está lista e não será inserido.')
 
  resposta = str(input('Deseja inserir mais um número [S/N]: ')).strip().upper()
  if resposta == 'N':
    break
numeros.sort()
print(f'Os números inseridos foram: {numeros}.')