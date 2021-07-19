# 55. Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0
for p in range(1, 6):
    pes = float(input('Peso da pessoa {}: '.format(p)))
    if p == 1:
        maior = pes
        menor = pes
    else:
        if pes > maior:
            maior = pes
        if pes < menor:
            menor = pes
print('O maior peso lido foi {}Kg.'.format(maior))
print('O menor peso lido foi {}Kg.'.format(menor))
