# 14. Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF:

c = float(input('Digite a temperatura em ºC: '))
f = ((9 * c) / 5) + 32
print('\033[36m{}ºC\033[m equivale a \033[32m{}ºF\033[m.'.format(c, f))
