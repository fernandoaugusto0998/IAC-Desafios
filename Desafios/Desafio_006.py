#Faça um programa que leia a largura e a altura de uma parede em metros,
#e calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada
#litro de tinta pinta uma área de 2 metros quadrados.

altura = float (input('Digite a altura da parade:'))
largura = float(input('Digite a largura da parede:'))

area = altura * largura

tinta = area / 2

print('Para pintar a área de {} é necessário {}L de tinta' .format(area, tinta))

