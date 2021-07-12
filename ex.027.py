# 27. Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente:

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é \033[94m{}\033[m.'.format(n[0]))
print('Seu último nome é \033[92m{}\033[m.'.format(n[len(n) - 1]))
