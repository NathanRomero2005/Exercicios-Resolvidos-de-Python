# 31. Desenvolva um programa que perrgunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando
# R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas:

d = int(input('Qual a distância da viagem (Km)? '))
if d <= 200:
    print('O valor total a ser cobrado é \033[92mR${:.2f}\033[m.'.format(d * 0.50))
else:
    print('O valor total a ser cobrado é \033[92mR${:.2f}\033[m.'.format(d * 0.45))
