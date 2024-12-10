"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {a:.1f}m²')


# Programa Principal
print('Controle de Terrenos')
print('=' * 30)
larg = float(input('LARGURA (em metros): '))
comp = float(input('COMPRIMENTO (em metros): '))
area(larg, comp)
