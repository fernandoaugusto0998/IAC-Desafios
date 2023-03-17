#Desenvolva um método que calcule o volume de uma caixa d'água
#retangular. Para tanto, pesquise como calcular o volume de um retângulo.

#import os

comprimento = float(input("COMPRIMENTO = "))
altura = float(input("ALTURA = "))
largura = float(input("LARGURA = "))

volume = comprimento * largura * altura

print("\nVOLUME = %.2f m³\n" % volume)

#os.system("pause")