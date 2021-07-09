# 10. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# (considere US$1.00 = R$3.27)

r = float(input('Quanto dinheiro você tem na cateira? R$ '))
d = r / 3.27
print('Com \033[32mR${:.2f}\033[m, você pode comprar \033[34mUS${:.2f}\033[m.'.format(r, d))
