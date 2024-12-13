"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)"""
def notas(*nota, sit=False):
    """
    Função recebe várias notas e armazena em um dicionário o total de notas, as maior e menor notas, média e situação da turma.
    :param nota: Notas da turma.
    :param sit: (Opcional) Mostra ou não a situação da turma.
    :return: Dicionário com as informações da turma.
    """
    t = dict()
    soma = 0
    for n in nota:
        soma += n
    media = soma / len(nota)
    t['total'] = len(nota)
    t['maior'] = max(nota)
    t['menor'] = min(nota)
    t['média'] = media

    if sit:
        if media < 5:
            t['situação'] = 'RUIM'
        elif media >= 7:
            t['situação'] = 'BOA'
        else:
            t['situação'] = 'RAZOÁVEL'

    return t

# Programa principal
turma = notas(6, 7.8, 6, 9, 7, 6.2, sit=True)
print(turma)