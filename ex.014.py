# 14. Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF:

c = float(input('Digite a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
print('{}ºC equivale a {}ºF.'.format(c, f))
