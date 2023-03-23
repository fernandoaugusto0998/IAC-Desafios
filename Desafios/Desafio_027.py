#Desenvolva um método que leia dois números reais e efetue as quatro
#perações entre eles.

x1  =  float ( input ( 'Informe o primeiro número: ' ))
x2  =  float ( input ( 'Informe o segundo número: ' ))

soma  =  x1 + x2
sub  =  x1 - x2
multi  =  x1 * x2
div  =  x1 / x2

print ( f' \n Soma de { x1 } + { x2 } = { soma :.2f}  ' )
print ( f'Subtração de { x1 } - { x2 } = { sub :.2f} ' )
print ( f'Multiplicação de { x1 } * { x2 } = { multi :.2f}' )
print ( f'Divisão de { x1 } / { x2 } = { div :.2f} ' )