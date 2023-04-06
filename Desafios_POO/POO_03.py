# POO_03 - Crie um programa que liste os funcionários contratados em determinado
# mês, informado pelo usuário.

from FakeDB import FakeDB


fakeDB = FakeDB()
mesPesquisa = input("Informe mês do contrato: ")

print(f'\nFuncionarios contratados no mês - {mesPesquisa}')
for funcionario in fakeDB.Funcionarios:
    mesFuncionario = funcionario.getDataCadastro()[2:4]
    if mesFuncionario == mesPesquisa:
        print(f'{funcionario.getNome()} | {funcionario.getDataCadastro()}')
