"""Aprimore o desafio anterior (86), mostrando no final:
A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha."""
matriz = [[], [], []]
total = 0
maior_valor = soma_terceira_coluna = 0
for l in range(0, 3):
  for v in range(0, 3):
    num = int(input(f'Digite um valor para {l, v}: '))
    matriz[l].append(num)
    
    if num % 2 == 0:
      total += num
    if v == 2:
      soma_terceira_coluna += num

print('=' * 30)
for i in matriz:
  print(f'[ {i[0]:^3} ] [ {i[1]:^3} ] [ {i[2]:^3} ]')

print('=' * 30)
print(f'A soma total de todos os valores pares é {total}.')
print(f'O soma dos valores da terceira coluna é {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
