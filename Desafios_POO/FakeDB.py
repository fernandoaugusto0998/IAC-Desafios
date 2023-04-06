from datetime import date
from datetime import datetime
from Funcionario import Funcionario



import csv

class FakeDB:

    Funcionarios = []

    def AutoFillFuncionarios(self):
        with open('Funcionarios.txt') as csvfile:
            linereader = csv.reader(csvfile, delimiter=';')
            for row in linereader:
                obj = Funcionario()
                obj.codigo = int(row[0])
                obj.nome = row[1]
                obj.sobrenome = row[2]
                obj.dataCadastro = row[3]
                self.Funcionarios.append(obj)


    def __init__(self):
        self.AutoFillFuncionarios()

