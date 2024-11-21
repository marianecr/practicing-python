"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."""

real = float(input('Digite quanto há disponível para conversão:R$ '))

dolares = real / 5.71 # Valor em 28/10/2024

print(f'Com R${real:.2f} é possível obter ${dolares:.2f}.')
