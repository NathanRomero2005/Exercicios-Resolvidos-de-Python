# 28. Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu:

from random import randint
from time import sleep
r = randint(0, 5)
print('Pensando em um número de 0 a 5. Tente adivinhar...')
sleep(2)
j = int(input('Em que número pensei? '))
sleep(2)
if j == r:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Você perdeu! Na verdade, pensei no número {}.'.format(r))
