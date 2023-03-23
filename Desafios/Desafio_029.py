#Desenvolva um método que calcula o valor de uma prestação em atraso,
#baseado em uma taxa de juros influenciada pelo usuário.

def  calcMulta ( taxaJuros , valorParcela , diasAtraso ):
    res  =  valorParcela  * (( 1  +  taxaJuros  /  100 ) **  diasAtraso )
    return res


valorParcela = float ( input ('Informe o valor da parcela sem multa (R$): '))
taxaJuros = int ( input ('Informe a taxa de juros diária (%): '))
diasAtraso = int ( input ('Informe a quantidade de dias em atraso: '))


valorMulta = calcMulta ( taxaJuros , valorParcela , diasAtraso )

print (f'O valor da parcela será de R$ {valorMulta :.2f} ' )
print (f'O valor total da multa será de R$ {valorMulta - valorParcela :.2f} ')