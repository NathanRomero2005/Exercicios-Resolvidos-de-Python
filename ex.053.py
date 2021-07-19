# 53. Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j) -1, -1, -1):
    i += j[l]
print(j, i)
if i == j:
    print('É um palíndromo!!')
else:
    print('Não é um palíndromo!!')
