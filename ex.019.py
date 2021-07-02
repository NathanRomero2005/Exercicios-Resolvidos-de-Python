# 19. Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome escolhido:

from random import choice
n1 = input('Digite o nome do(a) 1º aluno(a): ')
n2 = input('Digite o nome do(a) 2º aluno(a): ')
n3 = input('Digite o nome do(a) 3º aluno(a): ')
n4 = input('Digite o nome do(a) 4º aluno(a): ')
l = [n1, n2, n3, n4]
print('O aluno(a) escolhido(a) é {}.'.format(choice(l)))
