"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""

preco_atual = float(input('Digite o valor atual do produto: R$'))

novo_preco = preco_atual - (preco_atual * 0.05)

print(f'Com 5% de desconto, o produto passará de R${preco_atual:.2f} para R${novo_preco:.2f}.')
