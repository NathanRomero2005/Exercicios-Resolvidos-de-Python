# 5. Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:

n = int(input('Digite um número inteiro: '))
a = n - 1
s = n + 1
print('O \033[35mantecessor\033[m de \033[37m{}\033[m é \033[35m{}\033[m e seu \033[33msucessor\033[m é '
      '\033[33m{}\033[m.'.format(n, a, s))
