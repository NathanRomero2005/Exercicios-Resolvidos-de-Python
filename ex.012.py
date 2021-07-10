# 12. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto:

pi = float(input('Qual é o preço atual do produto? R$ '))
d = pi - (pi * 5 / 100)
print('O preço antes do desnconto era \033[31mR${:.2f}\033[m, e seu preço agora é \033[32mR${:.2f}\033[m.'.format(pi, d))
