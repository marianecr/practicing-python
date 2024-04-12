distancia = float(
    input("Qual foi a distância percorrida (em Km) com o carro? "))
dias = int(input("Por quantos dias o carro foi alugado? "))
valorTotal = (dias * 60) + (distancia * 0.15)

print(
    "Tendo percorrido {:.1f} km e alugado o carro por {} dias, o valor total a pagar será de R${:.2f}.".format(distancia, dias, valorTotal))
