def crescente(lista):
    
    size = []
    comprimento = len(lista)
    maior = 1
    size = [1 for x in range(comprimento)]
    if comprimento == 0:
       return 0
    
    for i in range(comprimento - 2, -1, -1):
        for j in range(i + 1, comprimento):    
            if lista[i] <= lista[j]:
                if maior < size[i] + size[j]:
                    maior = size[i] + size[j]
                
        size[i] = maior
        maior = 1

    return max(size)

# 100 %