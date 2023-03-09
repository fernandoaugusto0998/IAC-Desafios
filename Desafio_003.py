#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Informe o valor em metros:'))
mm = m * 1000

print('%.f A quantidade de metros equivalem á %.f milímetros:' %(m, mm))