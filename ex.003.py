# 3. Crie um programa que leia dois números e mostre a soma entre eles:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma entre \033[36m{}\033[m e \033[36m{}\033[m vale \033[31m{}\033[m.'.format(n1, n2, s))
