def metade(valor=0.0, formatar=False):
    """
    Calcula a metade do valor.
    :param valor: (Opcional) Valor a ser informado a sua metade
    :param formatar: (Opcional) Informar se o resultado deve ser formatado em moeda
    :return: Resultado do cálculo da metade do valor
    """
    mtd = valor / 2
    if formatar:
        mtd = moeda(mtd)
    return mtd

def dobro(valor=0.0, formatar=False):
    """
    Calcula o dobro do valor
    :param valor: (Opcional) Valor a ser calculado o seu dobro
    :param formatar: (Opcional) Informar se o resultado deve ser formatado em moeda
    :return: Resultado do cálculo do dobro do valor
    """
    dbr = valor * 2
    if formatar:
        dbr = moeda(dbr)
    return dbr

def aumentar(valor=0.0, taxa=0, formatar=False):
    """
    Calcula o resultado do aumento de uma taxa sobre o valor
    :param valor: (Opcional) Valor sobre o qual será aplicada a taxa
    :param taxa: (Opcional) Valor da taxa a ser aplicado sobre o valor
    :param formatar: (Opcional) Informar se o resultado deve ser formatado em moeda
    :return: Resultado do novo valor incrementado com a taxa
    """
    aumento = valor + (valor * (taxa / 100))
    if formatar:
        aumento = moeda(aumento)
    return aumento

def diminuir(valor=0.0, taxa=0, formatar=False):
    """
    Calculo o resultado do desconto de uma taxa sobre o valor
    :param valor: (Opcional) Valor sobre o qual será aplicado o desconto
    :param taxa: (Opcional) Valor da taxa a ser aplicada sobre o valor
    :param formatar: (Opcional) Informar se o resultado deve ser formatado em moeda
    :return: Resultado do novo valor com o desconto
    """
    diminuicao = valor - (valor * (taxa / 100))
    if formatar:
        diminuicao = moeda(diminuicao)
    return diminuicao

def moeda(valor=0.0, moeda='R$'):
    """
    Faz a formatação do valor no formato de moeda
    :param valor: Valor a ser formatado
    :param moeda: Moeda na qual será formatado o valor
    :return: Valor formatado
    """
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(valor=0.0, taxa_aumento=0, taxa_desconto=0):
    """
    Mostra um resumo reunindo os dados obtidos por meio das outras funções
    :param valor: (Opcional) Valor sobre o qual serão obtidos os dados
    :param taxa_aumento: (Opcional) Valor da taxa a se aumentar, que será passada à função aumentar()
    :param taxa_desconto: (Opcional) Valor da taxa a ser de desconto, que será passada à função diminuir()
    :return: Sem retorno
    """
    print('=' * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('=' * 30)

    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{taxa_aumento}% de aumento: \t{aumentar(valor, taxa_aumento, True)}')
    print(f'{taxa_desconto}% de desconto: \t{diminuir(valor, taxa_desconto, True)}')

    print('=' * 30)