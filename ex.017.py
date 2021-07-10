# 17. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa:

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('Considerando os valores dos catetos, a hipotenusa é \033[37m{:.2f}\033[m.'.format(hypot(co, ca)))
