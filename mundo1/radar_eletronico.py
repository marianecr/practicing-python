'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    excesso_velocidade = velocidade - 80
    multa = excesso_velocidade * 7
    
    print(f'A velocidade limite foi excedida em {excesso_velocidade} Km/h. Você terá que pagar uma multa de R${multa:.2f}.')
    print('Respeite as leis de trânsito!')