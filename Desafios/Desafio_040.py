
turma = ["Fernando0", "Fernando1","Fernando2","Fernando3","Fernando4","Fernando5",]
alturas = []
matriculas = []

def solicitarAltura():

    for i in turma:
        altura = float(input(f"Informe a altura do {i}: "))
        alturas.append(altura)

        matricula = int(input(f"Informe a matricula do {i}: "))
        matriculas.append(matricula)


    if max(alturas):
        inh = max(alturas)
        index = alturas.index(inh)
        print(f"O aluno mais alto mede {max(alturas)} - Matricula: {matriculas[index]}")

    if min(alturas)
        inh = min(alturas)
        index = alturas.index(inh)
        print(f"O aluno mais baixo mede {min(alturas)} - Matricula:{matriculas[index]}")


solicitarAltura()

