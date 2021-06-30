# 12. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto:

pi = float(input('Qual é o preço atual do produto? R$ '))
d = pi - (pi * 5 / 100)
print('O preço antes do desnconto era R${:.2f}, e seu preço agora é R${:.2f}.'.format(pi, d))
