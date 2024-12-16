def metade(valor=0):
    mtd = valor / 2
    return mtd

def dobro(valor=0):
    dbr = valor * 2
    return dbr

def aumentar(valor=0, taxa=0):
    aumento = valor + (valor * (taxa / 100))
    return aumento

def diminuir(valor=0, taxa=0):
    diminuicao = valor - (valor * (taxa / 100))
    return diminuicao

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

#valor_separado = str(valor).split(sep='.')
#valor_junto = ','.join(valor_separado) + '0'
#valor_formatado = 'R$' + valor_junto