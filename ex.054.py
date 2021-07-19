# 54. Crie que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas ja são maiores

from datetime import date
a = date.today().year
tMa = 0
tMe = 0
for p in range(1, 8):
    nasc = int(input('{}º ano: '.format(p)))
    i = a - nasc
    if i >= 21:
        tMa += 1
    else:
        tMe += 1
print('No total, foram {} pessoas maiores de idade.'.format(tMa))
print('No total, foram {} pessoas menores de idade.'.format(tMe))
