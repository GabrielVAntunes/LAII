def aux(soma, lista, comprimento_lista, indice, somasubseq):
    if comprimento_lista == 0:
        return 0

    for indice in range(len(lista)):
        somasubseq += lista[indice]
        if somasubseq > soma:
            return 0
        if somasubseq == soma:
            return soma

    return aux(soma, lista, comprimento_lista - 1, indice + 1, somasubseq)

def validas(soma, listas):
    resp = []
    for lista in listas:
        if aux(soma, lista, len(lista), 0, 0) == soma:
            resp.append(lista)

    return resp

# 90 %