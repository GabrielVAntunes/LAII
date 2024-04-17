def maxsoma(lista):

    max_atual = lista[0]
    max_total = lista[0]

    for num in lista[1:]:

        max_atual = max(num, max_atual + num)
        max_total = max(max_total, max_atual)

    return max_total

# 100 %