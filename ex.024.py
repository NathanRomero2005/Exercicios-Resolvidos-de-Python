# 24. Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO":

c = str(input('Em que cidade você nasceu? ')).strip()
print('\033[33m', c[:5].upper() == 'SANTO')
