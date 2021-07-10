# 11. Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessára para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados:

l = float(input('Qual a largura da parede, em metros? '))
h = float(input('Qual a altura da parede, em metros? '))
a = l * h
t = a / 2
print('A área da parede é \033[31m{:.2f}m²\033[m. A quantidade de tinta necessária é \033[34m{:.2f}l\033[m.'.format(a, t))
