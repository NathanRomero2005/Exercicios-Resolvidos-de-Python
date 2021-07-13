# 34. Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$ 1.250,00, calcule um aumento de 10%. para inferiores ou iguais, o aumento é de 15%:

s = float(input('Digite o salário: R$'))
if s > 1250.00:
    print('O salário de \033[92mR${:.2f}\033[m com reajuste de \033[93m10%\033[m, agora é \033[92mR${:.2f}\033[m.'
          .format(s, s + (s * 10 / 100)))
else:
    print('O salário de \033[92mR${:.2f}\033[m com reajuste de \033[93m15%\033[m, agora é \033[92mR${:.2f}\033[m.'
          .format(s, s + (s * 15 / 100)))
