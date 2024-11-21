"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

km_percorridos = float(input('Digite a distância percorrida (KM): '))
dias = int(input('Por quantos dias o carro foi alugado? '))
total = (dias * 60) + (km_percorridos * 0.15)

print(f'Para {dias} dias e {km_percorridos} quilômetros percorridos, o total será de R${total:.2f}.')
