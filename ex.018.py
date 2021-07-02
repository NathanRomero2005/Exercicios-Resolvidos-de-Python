# 18. Faça um programa que leia um ângulo qualquer e mostre na tela o valpor do seno, cosseno e tangente desse ângulo:

from math import sin, cos, tan, radians
a = int(input('Digite o valor de um ângulo qualquer: '))
print('O seno de {} é {:.2f}.'.format(a, sin(radians(a))))
print('O cosseno de {} é {:.2f}.'.format(a, cos(radians(a))))
print('A tangente de {} é {:.2f}.'.format(a, tan(radians(a))))
