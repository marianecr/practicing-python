"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""
expressao = str(input('Digite uma expressão matemática: ')).strip().lower()
if expressao.count('(') == expressao.count(')'):
  print('Sua expressão é válida.')
else:
  print('Sua expressão está incorreta.')
