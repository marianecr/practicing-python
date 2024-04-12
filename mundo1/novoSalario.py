salario = float(input("Digite o valor do salário atual: R$"))

novoSalario = salario + (salario * 0.15)

print("O salário passará de R${:.2f} para R${:.2f} com os 15% de aumento.".format(
    salario, novoSalario))
