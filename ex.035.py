# 35. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo:

r1 = float(input('Medida da primeira reta: '))
r2 = float(input('Medida da segunda reta: '))
r3 = float(input('Medida da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[92mPodem formar um triângulo\033[m.')
else:
    print('\033[91mNão podem formar um triângulo\033[m.')
