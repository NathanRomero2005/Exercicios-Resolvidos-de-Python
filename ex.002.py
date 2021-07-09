# 2. Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas:

nome = input('Digite seu nome: ')
print('Olá \033[32m{}\033[m! Muito prazer em te conhecer!'.format(nome))
