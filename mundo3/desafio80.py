"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""
numeros = []
for i in range(0, 5):
  num = int(input('Digite um número: '))
  if i == 0 or num > numeros[-1]: # Se num for o primeiro elemento inserido ou maior que o último elemento, insere no final da lista
    numeros.append(num)
    print('O número foi adicionado no final da lista.')
      
  else:
    pos = 0
    while pos < len(numeros): # Enquanto a posição for menor que o tamanho da lista
      if num <= numeros[pos]: # Número igual ou menor que o elemento na posição, insere o número nessa posição
        numeros.insert(pos, num)
        print(f'O número foi adicionado na posição {pos}.')
        break
      pos += 1
print(f'Os valores inseridos foram (em ordem): {numeros}.')
