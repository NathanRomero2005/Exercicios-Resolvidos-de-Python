# 4. Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele:

msg = input('Digite algo: ')
print('O tipo primitivo do que você digitou é {}.'.format(type(msg)))
print('O que você digitou só tem espaços?', msg.isspace())
print('O que você digitou é um número?', msg.isnumeric())
print('O que você digitou é alfabético?', msg.isalpha())
print('O que você digitou é alfanumérico?', msg.isalnum())
print('O que você digitou está em maiúsculas?', msg.isupper())
print('O que você digitou está em minúsculas?', msg.islower())
print('O que você digitou está capitalizado?', msg.istitle())
