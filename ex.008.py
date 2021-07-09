# 8. Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm, mm:

m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{}{}{}, em metros, equivale a {}{}{} Km;'.format('\033[33m', m, '\033[m', '\033[35m', km, '\033[m'))
print('{}{}{}, em metros, equivale a {}{}{} Hm;'.format('\033[33m', m, '\033[m', '\033[35m', hm, '\033[m'))
print('{}{}{}, em metros, equivale a {}{}{} Dam;'.format('\033[33m', m, '\033[m', '\033[35m', dam, '\033[m'))
print('{}{}{}, em metros, equivale a {}{}{} Dm;'.format('\033[33m', m, '\033[m', '\033[35m', dm, '\033[m'))
print('{}{}{}, em metros, equivale a {}{}{} Cm;'.format('\033[33m', m, '\033[m', '\033[35m', cm, '\033[m'))
print('{}{}{}, em metros, equivale a {}{}{} Mm.'.format('\033[33m', m, '\033[m', '\033[35m', mm, '\033[m'))
