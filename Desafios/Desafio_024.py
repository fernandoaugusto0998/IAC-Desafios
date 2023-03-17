#Desenvolva um método que calcule o volume de um Cilindro qualquer. Para
#tanto, pesquise como calcular o volume de um cilindro.

#import os

raio = float(input("RAIO = "))
altura = float(input("ALTURA = "))

volume = 3.14159 * raio ** 2 * altura

#print("\nVOLUME = %.4f m³\n" % volume)
print(f'O volume é: {volume:.4f} m³')

#s.system("pause")