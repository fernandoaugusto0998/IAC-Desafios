#Crie um programa que leia o quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$ 1,00 = R$ 5,00

n = float(input('Quantos reais você tem? \nR$'))

dolar = 5.00

compra = n / dolar

print('Com R${:.2f}, você pode comprar US${:.2f}.' .format(n, compra))
