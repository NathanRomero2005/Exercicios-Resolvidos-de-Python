# 6. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e  raiz quadrada:

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print('O número digitado foi {}. Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.3f}.'.format(n, d, t, r))
