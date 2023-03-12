#Crie um programa que leia um número e mostre o seu dobro, seu triplo e sua raiz quadrada.

n = int(input('Digite um número:'))
d = n*2
t = n*3
r = n **(1/2)

print('O dobro de {} é {}.' .format(n, d))
print('O triplo de {} é {}.' .format(n, t))
print('A raiz quadrade de {} é {:.2f}.' .format(n, r))
