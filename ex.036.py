# 36. Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal,
# sabendo qie ele não pode exceder 30% do salário ou então o empréstimoe será negado:

sal = float(input('Qual é o seu salário? R$'))
v = float(input('Qual é o valor da casa? R$'))
a = int(input('Em quantos anos você irá pagar? '))
p = v / (a * 12)
min = (sal * 30) / 100
if p <= min:
    print('Empréstimo CONCEDIDO!')
    print('O valor da prestação é {}.'.format(p))
else:
    print('Empréstimo NEGADO!')
