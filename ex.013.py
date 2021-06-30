# 13. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento:

si = float(input('Qual é o salário atual? R$ '))
r = si + (si * 15 / 100)
print('O salário antes do reajuste é era R${:.2f}, e o salário agora é R${:.2f}.'.format(si, r))
