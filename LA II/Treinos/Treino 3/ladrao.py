def ladrao(capacidade,objectos):
    objectos.sort(key = lambda x: x[1]/x[2], reverse = True)
    
    print(objectos)
    cap = 0
    lista_obj = []
    
    for objeto in objectos:
        cap += objeto[2]
        
        if cap <= capacidade:
            lista_obj.append(objeto)
            
    soma = 0
    for objeto in lista_obj:
        soma += objeto[1]
    return soma

# 80 %