# 44. Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

prec = float(input('Digite o preço do produto: R$'))
print('''Condições de pagamento:
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')
cond = int(input('Condição de pagamento: '))
if cond == 1:
    print('O total a ser pago é R${:.2f}.'.format(prec - (prec * 10 / 100)))
elif cond == 2:
    print('O total a ser pago é R${:.2f}.'.format(prec - (prec * 5 / 100)))
elif cond == 3:
    print('O total a ser pago é R${:.2f}.'.format(prec))
    print('Cada parcela será de R${:.2f}.'.format(prec / 2))
elif cond == 4:
    print('O total a ser pago é R${:.2f}.'.format(prec + (prec * 20 / 100)))
    parc = int(input('Nº de parcelas: '))
    print('Dividido em {}x, cada parcela será de R${:.2f}.'.format(parc, (prec + (prec * 20 / 100)) / parc))
