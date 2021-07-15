# 41. A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento: '))
i = ano - nasc
if i <= 9:
    print('É um(a) atleta MIRIM.')
elif 9 < i <= 14:
    print('É um(a) atleta INFANTIL.')
elif 14 < i <= 19:
    print('É um(a) atleta JÚNIOR.')
elif 19 < i <= 25:
    print('É um(a) atleta SÊNIOR.')
else:
    print('É uma(a) atleta MASTER.')
