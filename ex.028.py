# 28. Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu:

from random import randint
from time import sleep
r = randint(0, 5)
print('\033[93mPensando em um número de 0 a 5. Tente adivinhar...\033[m')
sleep(2)
j = int(input('Em que número pensei? '))
sleep(2)
if j == r:
    print('\033[92mParabéns!\033[m Você conseguiu me vencer!')
else:
    print('\033[91mVocê perdeu!\033[m Na verdade, pensei no número \033[91m{}\033[m.'.format(r))
