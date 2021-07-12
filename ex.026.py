# 26. Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A";
# 2. Em que posição ela aparece na primeira vez;
# 3. Em que posição ela aparece na última vez:

f = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece \033[93m{}\033[m vezes.'.format(f.count('A')))
print('A primeira letra A aparece na posição \033[96m{}\033[m.'.format(f.find('A') + 1))
print('A última letra A aparece na posição \033[95m{}\033[m.'.format(f.rfind('A') + 1))
