# 23. Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados:

num = int(input('Digite um número de 0 até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: \033[96m{}\033[m.'.format(u))
print('Dezena: \033[93m{}\033[m.'.format(d))
print('Centena: \033[92m{}\033[m.'.format(c))
print('Milhar: \033[94m{}\033[m.'.format(m))
