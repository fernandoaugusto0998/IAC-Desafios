# POO_02 - Crie um programa que liste os funcionários que fazem aniversário de
# contrato em determinado ano, informado pelo usuário.

from FakeDB import FakeDB


fakeDB = FakeDB()
mesPesquisa = input("Informe mês do contrato: ")
anoPesquisa = input("Informe ano do contrato: ")
pesquisaAniver = mesPesquisa+anoPesquisa

print(f'\nFuncionarios que fazem aniversario de contrato - Mes {mesPesquisa} em {anoPesquisa}')
for funcionario in fakeDB.Funcionarios:
    if funcionario.getDataCadastro().endswith(pesquisaAniver):
        nome = funcionario.getNome()
        data = funcionario.getDataCadastro()
        print(f'{nome} - {data}')
