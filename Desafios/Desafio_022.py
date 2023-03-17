#Desenvolva um método que calcule o IMC de uma determinada pessoa. Para
#tanto, pesquise como funciona o cálculo do IMC.


peso = float(input('Informe quantos kg você tem: '))
altura = float(input('Informe a sua altura: '))

imc = peso / altura ** 2

if imc < 18.5:
    print('Magrelo')

elif (imc > 18.5) and (imc <25.0):
    print('Tá na ideia')

elif (imc > 25.0) and (imc <30.0):
    print('Ta gordão mano')

elif (imc > 30.0) and (imc <40.0):
    print('Nem guindaste mano!')

