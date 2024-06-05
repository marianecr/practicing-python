'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

r1 = float(input('Digite o valor do tamanho da primeira reta: '))
r2 = float(input('Digite o valor do tamanho da segunda reta: '))
r3 = float(input('Digite o valor do tamanho da terceira reta: '))

if (r1 < r2 + r3) and (r2 < r3 + r1) and (r3 < r2 + r1):
    print(f'Com retas de tamanho {r1}, {r2} e {r3} é possível formar um ▲.')
else:
    print('Não é possível formar um triângulo.')