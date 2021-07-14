# 39. Faça um programa que leia a data de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento: '))
i = ano - nasc
print('Você tem/terá {} anos.'.format(i))
if i == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!!')
elif i < 18:
    print('Você ainda não precisa se alistar! Ainda faltam {} anos para seu alistamento.'.format(18 - i))
else:
    print('Você já deveria ter se alistado! Isso deveria ter sido há {} anos.'.format(i - 18))
