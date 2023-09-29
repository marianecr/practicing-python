def contagem_crescente(numero, numeroLimite):
    if numero <= numeroLimite:
        print(numero, end=" ")
        contagem_crescente(numero + 1, numeroLimite)


limite = int(input("Digite o número até o qual deseja realizar a contagem: "))

contagem_crescente(0, limite)
