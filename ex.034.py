# 34. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$ 1.250,00, calcule um aumento de 10%. para inferiores ou iguais, o aumento é de 15%:

s = float(input('Digite o salário: R$'))
if s > 1250.00:
    print('O salário de R${:.2f} com reajuste de 10%, agora é R${:.2f}.'.format(s, s + (s * 10 / 100)))
else:
    print('O salário de R${:.2f} com reajuste de 15%, agora é R${:.2f}.'.format(s, s + (s * 15 / 100)))
