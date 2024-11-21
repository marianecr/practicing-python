"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas."""

distancia = float(input('Digite a distância da viagem: '))

if distancia <= 200:
    passagem = distancia * 0.50
    print(f'Para uma viagem de {distancia} km, a passagem custará R${passagem:.2f}.')
else:
    passagem = distancia * 0.45
    print(f'Para uma viagem de {distancia} km, a passagem custará R${passagem:.2f}.')

print('Tenha uma boa viagem!')