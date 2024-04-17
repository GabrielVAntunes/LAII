def isbn(livros):
    invalidos = []

    for livro in livros:
        digito = 0
        posicao = 0
        numero = livros[livro]

        while (posicao <= 12):
            if posicao % 2 == 1:
                digito += int(numero[posicao]) * 3
            else:
                digito += int(numero[posicao]) * 1
            posicao += 1
        if digito % 10 != 0:
            invalidos.append(livro)
            invalidos.sort()

    return invalidos

# 100 %
