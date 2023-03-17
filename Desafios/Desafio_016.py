## Desenvolva um método que solicite a entrada de um número e calcule se o
##número é par ou ímpar.


n = int(input('Digite um número:'))

resto = n % 2

if resto == 0:
    print('O número é par')

else:
    print('o número é inpar')

