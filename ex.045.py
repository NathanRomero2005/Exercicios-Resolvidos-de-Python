# 45. Crie um programa que faça o computador jogar Jokempô com você

from random import randint
i = ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2)
print('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
j = int(input('Sua escolha: '))
print('-=' * 15)
print('O computador jogou {}.'.format(i[c]))
print('O jogador jogou {}.'.format(i[j]))
print('-=' * 15)
if c == 0:
    if j == 0:
        print('EMPATE')
    elif j == 1:
        print('VITÓRIA DO JOGADOR')
    elif j == 2:
        print('VITÓRIA DO COMPUTADOR')
    else:
        print('JOGADA INVÁLIDA!')
elif c == 1:
    if j == 0:
        print('VITÓRIA DO COMPUTADOR')
    elif j == 1:
        print('EMPATE')
    elif j == 2:
        print('VITÓRIA DO JOGADOR')
    else:
        print('JOGADA INVÁLIDA!')
elif c == 2:
    if j == 0:
        print('VITÓRIA DO JOGADOR')
    elif j == 1:
        print('VITÓRIA DO COMPUTADOR')
    elif j == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
