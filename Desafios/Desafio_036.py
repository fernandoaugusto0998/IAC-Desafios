# Desafio 36 - Uma pessoa só pode votar em eleições brasileiras se ela for maior que 16 anos
# e for cidadã brasileira. Desenvolva um método que leia uma lista previamente carregada
# com o nome de 10 pessoas. Em seguida, solicite a idade da pessoa, e sua nacionalidade,
# armazenando em listas paralelas. Por fim, verifique quantas pessoas estão aptas a votar
# ou não, de acordo com os dados armazenados.

nomes = ['João', 'Maria', 'Pedro', 'Lucas', 'Ana', 'Márcia', 'Felipe', 'Fernanda', 'José', 'Carlos']
idades = []
nacionalidades =[]

def verifica_voto():
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    RESET = '\033[0;0m'

for nome in nomes:
    idade = int(input(f"Digite a idade de {nome}: "))
    nacionalidade = str(input(f"Informe a nacionalidade de {nome}: "))
    idades.append(idade)
    nacionalidades.append(nacionalidade)

    if idades > 16 and nacionalidades :
        print(f'{GREEN} Pode votar! {RESET}')

verifica_voto()
