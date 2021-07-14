# 40. Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('\033[91mREPROVADO\033[m')
elif 5.0 <= m <= 6.9:
    print('\033[93mRECUPERAÇÃO\033[m')
else:
    print('\033[92mAPROVADO\033[m')
