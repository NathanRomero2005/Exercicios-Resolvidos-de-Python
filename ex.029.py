# 29. Escreva um programa que leia a velocidade de um carro. Se ele ultrapasasr 80 km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite:

v = float(input('Qual a velocidade do carro (Km/h)? '))
m = (v - 80) * 7
if v > 80:
    print('Você foi multado!')
    print('O valor total a ser pago é R${:.2f}.'.format(m))
else:
    print('Você está dentro do limite permitido, continue assim!')
