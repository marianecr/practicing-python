valor_casa = float(input("Informe o valor total da casa: R$"))
salario = float(input("Informe o valor do seu salário: R$"))
anos_a_dividir = int(input("Em quantos anos pretende pagar? "))

prestacao_mensal = (valor_casa / anos_a_dividir) / 12

print(f"Com a casa no valor de R${valor_casa:.2f}, pagando em {anos_a_dividir} anos, a prestação seria de R${prestacao_mensal:.2f}.")

if prestacao_mensal > salario*0.3:
    print("Infelizmente, seu empréstimo foi negado.")

else:
    print("Parabéns!🎉 Seu empréstimo foi aprovado.")