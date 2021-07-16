# 50. Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que forem pares. Se o valor
# digitado for ímpar, desconsidere-o

s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        s += num
        cont += 1
print('Foram informados {} números PARES.'.format(cont))
print('A soma dos PARES equivale a {}.'.format(s))
