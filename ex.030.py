# 30. Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar:

num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número \033[93m{}\033[m é \033[93mpar\033[m!'.format(num))
else:
    print('O número \033[93m{}\033[m é \033[93mímpar\033[m!'.format(num))
