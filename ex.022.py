# 22. Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas;
# 2. O nome com todas as letras minúsculas;
# 3. Quantas letras tem, sem considerar espaços;
# 4. Quantas letras tem o primeiro nome:

nome = str(input('Digite seu nome completo: ')).strip()
ns = nome.split()
print('Seu nome com todas as letras maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas é: {}.'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(len(ns[0])))
