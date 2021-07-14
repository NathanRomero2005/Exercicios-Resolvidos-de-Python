# 37. Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
op = int(input('Sua opção: '))
if op == 1:
    print('O binário de {} é {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('O octal de {} é {}.'.format(num, oct(num)[2:]))
elif num == 3:
    print('O hexadecimal de {} é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
