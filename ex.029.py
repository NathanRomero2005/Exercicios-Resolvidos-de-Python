# 29. Escreva um programa que leia a velocidade de um carro. Se ele ultrapasasr 80 km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite:

v = float(input('Qual a velocidade do carro (Km/h)? '))
m = (v - 80) * 7
if v > 80:
    print('\033[31mVocê foi multado!\033[m')
    print('O valor total a ser pago é \033[92mR${:.2f}\033[m.'.format(m))
else:
    print('\033[92mVocê está dentro do limite permitido, continue assim!\033[m')
