# 6. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e  raiz quadrada:

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print('O número digitado foi \033[31m{}\033[m. Seu \033[34mdobro\033[m é \033[34m{}\033[m, seu \033[32mtriplo\033[m é '
      '\033[32m{}\033[m e sua \033[36mraiz quadrada\033[m é \033[36m{:.3f}\033[m.'.format(n, d, t, r))
