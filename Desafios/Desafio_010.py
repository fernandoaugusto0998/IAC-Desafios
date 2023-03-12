#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado,
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Informe a kilometragem do veículo: '))
dias = int(input('Informe quantos dias de uso: '))
#valortotal = (0.15 * km) + (60 * dias)
#print(f'O valor a ser pago é R${valortotal}')

aluguel = 60.00
km_rodado = 0.15
valor1 = km * km_rodado
valor2 = dias * aluguel
total = valor1 + valor2
print(f'O valor a ser pago é R${total}')
