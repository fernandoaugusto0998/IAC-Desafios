import random

nomeAluno = []

#for i in range(0 , 5):
  #  nomeAluno.append(input('Informe o nome do Aluno: '))


while True:
    nomesAluno = input('Informe o nome do Aluno: ')
    if nomesAluno != '0':
        nomeAluno.append(nomesAluno)
    else:
        print('Lista de alunos: \n{}'.format(nomeAluno))
        #print(f'Lista de alunos: \n {nomeAluno}')
        break

#nomeAluno.sort()
#aluno = random.choice(nomeAluno)
#print(f'Aluno: {aluno}')

sorteados = random.sample(nomeAluno, len(nomesAluno))
escolhido = random.choice(sorteados)
print('Lista de alunos: \n{}'.format(sorteados))
#for valor in sorteados:
print(f'Aluno sorteado: {escolhido}')
