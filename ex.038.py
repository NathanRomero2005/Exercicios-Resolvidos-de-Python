# 38. Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Os dois valores são iguais

n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))

if n1 > n2:
    print('O número \033[94m{}\033[m é maior que o \033[93m{}\033[m.'.format(n1, n2))
elif n2 > n1:
    print('O número \033[94m{}\033[m é maior que o \033[93m{}\033[m.'.format(n2, n1))
else:
    print('\033[94mOs dois números têm o mesmo valor\033[m')
