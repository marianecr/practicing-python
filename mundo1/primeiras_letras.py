'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO” '''

cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()

cidade_dividida = cidade.split()

print(f'A cidade {cidade} começa com "SANTO"? {"SANTO" in cidade_dividida[0]}')

