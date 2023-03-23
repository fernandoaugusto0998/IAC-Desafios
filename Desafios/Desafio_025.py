#Desenvolva um método que calcula o quadrado da diferença entre dois
#números quaisquer. Para tanto, pesquise como funcionam os métodos matemáticos em
#Pitão.

x1  =  int ( input ( 'Informe o primeiro número: ' ))
x2  =  int ( input ( 'Informe o segundo número: ' ))

resultado  = ( x1 - x2 ) ** 2
resultado2  = ( x1 ** 2 ) -  2 * x1 * x2  + ( x2 ** 2 )

print ( f'O quadrado da diferença entre { x1 } e { x2 } é > { resultado } > { resultado2 } ' )