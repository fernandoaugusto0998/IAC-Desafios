#Desenvolva um método que permita a entrada do nome do usuário e exiba:
#- Imprima a frase “Olá meu nome é: {nome recebido}”.
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.


nome = str(input('Informe o seu nome: '))
nome1 = nome.upper()
nome2 = nome.lower()
nome3 = len(nome.replace(" ", ""))
nome4 = len(nome.split()[0])

print('Olá meu nome é {}' .format((nome)))
print(nome2)
print(nome1)
print('O seu nome tem {} letras e o seu Primeiro nome tem {} letras' .format(nome3, nome4))
