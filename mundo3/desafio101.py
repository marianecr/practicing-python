"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""
def voto(nasc):
    """
    Função calcula a idade da pessoa e informa se o voto é obrigatório, opcional ou não vota.
    :param nasc: Ano de nascimento da pessoa
    :return: Sem retorno
    """
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - nasc

    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA AINDA.')
    elif 18 <= idade <=69:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {idade} anos: VOTO FACULTATIVO.')


ano_nascimento = int(input('Qual ano de nascimento? '))
voto(ano_nascimento)
