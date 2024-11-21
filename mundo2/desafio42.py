"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta2 + reta1):
    print(f'Com retas de tamanhos {reta1:.1f}, {reta2:.1f} e {reta3:.1f} é possível formar um triângulo.')

    if reta1 == reta2 == reta3:
        print('Todos os lados são iguais. Seria um triângulo EQUILÁTERO.')

    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('Dois lados são iguais. Seria um triângulo ISÓSCELES.')

    else:
        print('Todos os lados são diferentes. Seria um triângulo ESCALENO.')
else:
    print('Não é possível formar um triângulo.')