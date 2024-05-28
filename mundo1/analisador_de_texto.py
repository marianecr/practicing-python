''' Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = input('Digite seu nome completo: ').strip()

nome_dividido = nome.split()
nome_sem_espaco = ''.join(nome_dividido)

print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')
print(f'Total de letras: {len(nome_sem_espaco)}')
print(f'''Primeiro nome: {nome_dividido[0]}
Total de letras do primeiro nome: {len(nome_dividido[0])}''')