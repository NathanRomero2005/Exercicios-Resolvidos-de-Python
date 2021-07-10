# 13. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento:

si = float(input('Qual é o salário atual? R$ '))
r = si + (si * 15 / 100)
print('O salário antes do reajuste era \033[33mR${:.2f}\033[m, e o salário agora é \033[35mR${:.2f}\033[m.'.format(si, r))
