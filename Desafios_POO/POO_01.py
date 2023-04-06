# POO_01 - Crie um programa que liste os funcionários pelo nome, utilizando as 3
# primeiras letras do nome, informadas pelo usuário. Por exemplo, procure todos os
# funcionários cujo nome comece com as letras MAR.

from FakeDB import FakeDB


fakeDB = FakeDB()
pesquisaNome = input("Informe as 3 primeiras letras para pesquisa: ").lower()

for funcionario in fakeDB.Funcionarios:
    if funcionario.getNome().lower().startswith(pesquisaNome):
        nome = funcionario.getNome()
        print(f'{nome}')
