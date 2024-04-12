def lerAnoDeNascimento():
    anoDeNascimento = int(input("Digite o ano do seu nascimento: "))

    return anoDeNascimento


def lerAnoAtual():
    anoAtual = int(input("Digite o ano atual: "))

    return anoAtual


def calcularIdade():
    idade = lerAnoAtual() - lerAnoDeNascimento()

    return idade


def verificarMaioridade(idade):
    if idade < 18:
        print("Você ainda tem %d anos de idade. Por favor, apresente o documento da pessoa responsável." % idade)

    else:
        print("Você já possui %d anos. Apresente o seu documento de identificação, por favor." % idade)


verificarMaioridade(calcularIdade())
