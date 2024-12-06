"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas;
B) Uma listagem com as pessoas mais pesadas;
C) Uma listagem com as pessoas mais leves."""
pessoas = []
individuo = []
maior_peso = menor_peso = 0
pessoas_mais_pesada = []
pessoas_mais_leve = []
while True:
  nome = str(input('Nome: ')).strip()
  peso = float(input('Peso: '))
  individuo.append(nome)
  individuo.append(peso)

  if len(pessoas) == 0: # Se for o primeiro a ser adicionado na lista, maior e menor recebem o mesmo valor
    maior_peso = menor_peso = individuo[1]
  else:
    if individuo[1] > maior_peso:
      maior_peso = individuo[1]
    if individuo[1] < menor_peso:
      menor_peso = individuo[1]

  pessoas.append(individuo[:])
  individuo.clear()

  res = str(input('Deseja cadastrar mais alguém [S/N]? ')).strip().upper()
  if res == 'N':
    break

for p in pessoas: # Verifica o nome das pessoas mais leves e mais pesadas a adiciona nas respectivas listas
  if p[1] == maior_peso:
    pessoas_mais_pesada.append(p[0])
  if p[1] == menor_peso:
    pessoas_mais_leve.append(p[0])

print('-*' * 25)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}kg. Peso de {pessoas_mais_pesada}.')
print(f'O menor peso doi de {menor_peso}kg. Peso de {pessoas_mais_leve}')
