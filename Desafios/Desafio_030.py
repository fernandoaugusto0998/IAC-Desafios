#Desenvolva um método que identifica o maior e o menor número dentre 5
#números fornecidos pelo usuário.

numeros  = []
eu = 0

enquanto  i < 5 :
    num  =  int ( input ( 'Digite um numero: ' ))
    numeros . anexar ( num )
    eu  =  eu  +  1

imprimir ( números )

print ( f' \n O número maior é { max ( numeros ) } eo menor número é { min ( numeros ) } ' )