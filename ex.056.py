# 56. Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# > A média de idade do grupo
# > Qual é o nome do homem mais velho
# > Quantas mulheres têm menos de 20 anos

somaIdade = 0
medIdade = 0
maIdH = 0
nomeVelho = ''
totMul = 0
for p in range(1, 5):
    print('---- {}ª pessoa ----'.format(p))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()
    somaIdade += i
    if p == 1 and s in 'Mm':
        maIdH = i
        nomeVelho = n
    if s in 'Mm' and i > maIdH:
        maIdH = i
        nomeVelho = n
    if s in 'Ff' and i < 20:
        totMul += 1
medIdade = somaIdade / 4
print('A média das idades é {} anos.'.format(medIdade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomeVelho, maIdH))
print('No total, são {} mulheres com menos de 20 anos.'.format(totMul))
