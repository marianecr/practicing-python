"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

largura = float(input("Digite a largura, em metros, da parede: "))
altura = float(input("Digite a altura, em metros, da parede: "))
area = largura * altura

qtdTinta = area / 2

print(
    f"Para pintar uma parede de {area}m², você precisará de {qtdTinta} litros de tinta."
)
