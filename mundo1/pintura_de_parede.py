largura = float(input("Digite a largura, em metros, da parede: "))
altura = float(input("Digite a altura, em metros, da parede: "))
area = largura * altura

qtdTinta = area / 2

print(
    f"Para pintar uma parede de {area}m², você precisará de {qtdTinta} litros de tinta."
)
