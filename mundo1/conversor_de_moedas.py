'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

dinheiro = float(
    input("Digite a quantidade, em reais, que deseja converter: R$")
)

dolares = round(dinheiro / 4.88, 2)
print("Com R${:.2f} você pode ter US${:.2f}.".format(dinheiro, dolares))
