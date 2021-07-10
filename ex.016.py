# 16. Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira:

from math import trunc
num = float(input('Digite um número Real qualquer: '))
print('A parte inteira de \033[33m{}\033[m é \033[33m{}\033[m.'.format(num, trunc(num)))
