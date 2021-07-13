# 32. Faça um programa que leia um ano qualquer e mostre se ele é bissexto:

from datetime import date
a = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
    print('O ano \033[91m{}\033[m é \033[91mbissexto\033[m!'.format(a))
else:
    print('O ano \033[91m{} não\033[m é \033[91mbissexto\033[m!'.format(a))
