#Desenvolva um método que solicite a entrada de uma frase, após isto troque
#todas as letras ‘A’ ou ‘a’ por &. Para tanto, pesquise como funciona o método
#String.Replace().

nome = str(input('Digite uma frase: '))
nome1 = ""

if nome.count("A") >0 or nome.count("a") > 0:
    nome1 = nome.replace("A", "&")
    nome2 = nome1.replace("a", "&")

    print(nome2)

