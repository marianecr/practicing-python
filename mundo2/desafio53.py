"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
frase_dividida = frase.split()
frase_sem_espaco = ''.join(frase_dividida)
invertida = ''

for i in range(len(frase_sem_espaco) - 1, -1, -1):
    invertida += frase_sem_espaco[i]

if invertida == frase_sem_espaco:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')