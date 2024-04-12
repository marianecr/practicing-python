def soma(n1, n2):
    soma = n1 + n2
    return soma


def subtracao(n1, n2):
    subtracao = n1 - n2
    return subtracao


def multiplicacao(n1, n2):
    multi = n1 * n2
    return multi


def divisao(n1, n2):
    div = n1 / n2
    return div


def moduloDivisao(n1, n2):
    modulo = n1 % n2
    return modulo


op = int(input("""Escolha a operação que deseja realizar (digite o número correspondente):
 1 - Soma
 2 - Subtração
 3 - Multiplicação
 4 - Divisão
 Opção: """))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match op:
    case 1:
        res = soma(num1, num2)

        print(f"A soma entre {num1} e {num2} é igual a {res}.")

    case 2:
        res = subtracao(num1, num2)

        print(f"{num1} menos {num2} é igual a {res}.")

    case 3:
        res = multiplicacao(num1, num2)

        print(f"O produto entre {num1} e {num2} é {res}.")

    case 4:
        res = divisao(num1, num2)
        resto = moduloDivisao(num1, num2)

        print(f"{num1} divido por {num2} é igual a {res:.1f} e seu módulo é {resto}.")

    case _:
        print("Opção de operação inválida.")
