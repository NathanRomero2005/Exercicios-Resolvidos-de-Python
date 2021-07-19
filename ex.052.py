# 52. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

n = int(input('Digite um número inteiro: '))
nd = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        nd += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('O número {} foi divisível {} vezes.'.format(n, nd))
if nd == 2:
    print('Sendo assim, é um número primo.')
else:
    print('Sendo assim, não é um número primo.')
