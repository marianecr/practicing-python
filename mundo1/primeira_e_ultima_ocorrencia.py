'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase qualque: ')).strip().upper()

print(f'Frase: {frase}')
print(f'''Quantidade de A: {frase.count("A")}
Primeira ocorrência na posição {frase.find("A")+1} e última ocorrência na posição {frase.rfind("A")+1}.''')
