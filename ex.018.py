# 18. Faça um programa que leia um ângulo qualquer e mostre na tela o valpor do seno, cosseno e tangente desse ângulo:

from math import sin, cos, tan, radians
a = int(input('Digite o valor de um ângulo qualquer: '))
print('O seno de \033[94m{}\033[m é \033[93m{:.2f}\033[m.'.format(a, sin(radians(a))))
print('O cosseno de \033[94m{}\033[m é \033[93m{:.2f}\033[m.'.format(a, cos(radians(a))))
print('A tangente de \033[m{}\033[m é \033[93m{:.2f}\033[m.'.format(a, tan(radians(a))))
