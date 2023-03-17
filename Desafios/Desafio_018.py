#Desenvolva uma calculadora, onde será necessário entrar com a operação,
#primeiro e segundo valor, exiba o resultado na tela.

numero1 = int(input('Digite o primeiro número: '))
operaçao = input('Digite uma operação:')
numero2 = int(input('Digite o segundo número: '))

if operaçao == '+':
    print('{} + {} = '.format(numero1, numero2))
    print(numero1 + numero2)

elif operaçao == '-':
    print('{} - {} = '.format(numero1, numero2))
    print(numero1 - numero2)

elif operaçao == '*':
    print('{} * {} = '.format(numero1, numero2))
    print(numero1 * numero2)

elif operaçao == '/':
    print('{} / {} = '.format(numero1, numero2))
    print(numero1 / numero2)

else:
    print('Digite uma operação válida.')