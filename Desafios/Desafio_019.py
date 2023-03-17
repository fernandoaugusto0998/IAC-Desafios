#Desenvolva um método que solicite a entrada da idade de um determinado
#usuário, se for menor que 18 anos exiba na cor vermelha “Sem permissão”, caso seja maior
#ou igual a 18 anos exiba na cor verde “Permissão concedida”. Para tanto, pesquise como
#funciona o uso de cores no Python.

def verifica_idade():
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    RESET = '\033[0;0m'

    idade = int(input('Digite a sua idade: '))

    if idade <18:
        print(f'{RED} Sem permissão {RESET}')

    else:
        print(f'{GREEN} Permissão concedida!')

verifica_idade()