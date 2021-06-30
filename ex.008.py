# 8. Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm, mm:

m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{} em metros equivale a {} quilometros;'.format(m, km))
print('{} em metros equivale a {} hectômetros;'.format(m, hm))
print('{} em metros equivale a {} decâmetros;'.format(m, dam))
print('{} em metros equivale a {} decímetros;'.format(m, dm))
print('{} em metros equivale a {} centímetros;'.format(m, cm))
print('{} em metros equivale a {} milímetros.'.format(m, mm))
