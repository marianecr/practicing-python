"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores."""
from time import sleep
cores = ('\033[m',          # 0 - Sem cor
         '\033[0;30;41m',   # 1 - laranja avermelhado
         '\033[0;30;42m',   # 2 - verde
         '\033[0;30;43m',   # 3 - amarelo
         '\033[0;30;44m',   # 4 - lilás
         '\033[0;30;45m',   # 5 - rosa
         '\033[0;30;47m',   # 6 - cinza
         '\033[7;30m'       # 7 - Preto
         )
def ajuda():
    while True:

        print('\033[0;30;44m=' * 25)
        print(' SISTEMA DE AJUDA PyHELP')
        print('\033[0;30;44m=' * 25)

        msg = str(input('\033[mFunção ou Biblioteca >>> ')).strip()

        if msg.upper() == 'FIM':
            break
        print('\033[0;30;46m=' * (len(msg) + 32))
        print(f' Acessando o manual do comando {msg}')
        print('=' * (len(msg) + 32))

        sleep(1.5)
        print('\033[0;30;47m')
        help(msg)
        sleep(1.5)

ajuda()