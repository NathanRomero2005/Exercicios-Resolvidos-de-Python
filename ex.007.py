# 7. Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média entre as notas {}{:.1f}{} e {}{:.1f}{} é {}{:.1f}{}'.format('\033[37m', n1, '\033[m', '\033[37m', n2,
                                                                           '\033[m', '\033[34m', m, '\033[m'))
