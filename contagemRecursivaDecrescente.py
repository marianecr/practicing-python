def contagemDecrescente(n):
    if n < 0:
        return 0

    print(n, end=" ")

    return contagemDecrescente(n - 1)


numero = int(input("Digite um número inteiro para fazer a contagem: "))
contagemDecrescente(numero)
