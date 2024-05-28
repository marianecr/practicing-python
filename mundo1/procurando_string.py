'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nome = str(input('Digite um nome completo: ')).strip().upper()
nome_dividido = nome.split()

print(f'Há "SILVA" no nome {nome}? {"SILVA" in nome_dividido}')