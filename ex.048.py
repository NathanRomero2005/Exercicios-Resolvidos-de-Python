# 48. Faça um programa que calcule a some entre todos os números ímpares que são múltiplos de três e que se encontram
# no intervalo de 1 até 150

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print('A soma de todos os valores é {}.'.format(s))
print('Foram encontrados {} valores.'.format(cont))