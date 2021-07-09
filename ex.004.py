# 4. Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele:

msg = input('Digite algo: ')
print('O \033[33mtipo primitivo\033[m do que você digitou é {}.'.format(type(msg)))
print('O que você digitou só tem \033[33mespaços\033[m?', msg.isspace())
print('O que você digitou é um \033[33mnúmero\033[m?', msg.isnumeric())
print('O que você digitou é \033[33malfabético\033[m?', msg.isalpha())
print('O que você digitou é \033[33malfanumérico\033[m?', msg.isalnum())
print('O que você digitou está em \033[33mmaiúsculas\033[m?', msg.isupper())
print('O que você digitou está em \033[33mminúsculas\033[m?', msg.islower())
print('O que você digitou está \033[33mcapitalizado\033[m?', msg.istitle())
