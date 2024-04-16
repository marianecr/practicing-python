'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

distancia = float(input("Qual foi a distância percorrida (em Km) com o carro? "))
dias = int(input("Por quantos dias o carro foi alugado? "))
valorTotal = (dias * 60) + (distancia * 0.15)

print(
    "Tendo percorrido {:.1f} km e alugado o carro por {} dias, o valor total a pagar será de R${:.2f}.".format(distancia, dias, valorTotal))
