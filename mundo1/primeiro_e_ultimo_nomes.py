'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input('Digite seu nome completo: ')).strip()

nome_dividido = nome.split()

print(f'''Nome: {nome}
Primeiro nome: {nome_dividido[0]}
Último nome: {nome_dividido[-1]}''')