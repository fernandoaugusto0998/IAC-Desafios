# POO_05 - Crie um programa que busque e liste os funcionários que tenham as 3
# letras determinadas no sobrenome, informadas pelo usuário. Por exemplo, procure
# todos os funcionários que tenham as letras SAN no sobrenome.

from FakeDB import FakeDB


fakeDB = FakeDB()
letrasSobrenome = input("Informe as 3 primeiras letras do SOBRENOME para pesquisa: ").lower()

for funcionario in fakeDB.Funcionarios:
    if funcionario.getSobrenome().lower().startswith(letrasSobrenome):
        print(f'{funcionario.getNome()} - {funcionario.getSobrenome()}')