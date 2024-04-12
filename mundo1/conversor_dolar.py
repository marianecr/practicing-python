dinheiro = float(
    input("Digite a quantidade, em reais, que deseja converter: R$")
)

dolares = round(dinheiro / 4.88, 2)
print("Com R${:.2f} você pode ter US${:.2f}.".format(dinheiro, dolares))
