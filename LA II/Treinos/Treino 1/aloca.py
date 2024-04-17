def aloca(prefs):

    lista_nalocados = []
    alunos = sorted(prefs)
    lista_projetos = []

    for aluno in alunos:
        for projeto in prefs[aluno]:

            if projeto not in lista_projetos:
                lista_projetos.append(projeto)
                break
        else:
            lista_nalocados.append(aluno)

    return lista_nalocados

# 100 %
