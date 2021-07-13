# 33. Faça um programa que leia três números e mostre qual é o maior e qual é o menor:

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O \033[94mmaior\033[m valor digitado foi \033[94m{}\033[m.'.format(maior))
print('O \033[31mmenor\033[m valor digitado foi \033[31m{}\033[m.'.format(menor))
