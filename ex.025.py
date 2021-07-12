# 25. Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome:

n = str(input('Qual é seu nome completo? ')).strip().upper()
print('Seu nome tem Silva? \033[91m{}\033[m'.format('SILVA' in n.upper()))
