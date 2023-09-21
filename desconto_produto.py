preco = float(input("Digite o valor do produto: R$"))
novoPreco = preco - (preco * 0.05)

print("O produto de R${:.2f} sairá por R${:.2f} após ter 5% de desconto.".format(
    preco, novoPreco))
