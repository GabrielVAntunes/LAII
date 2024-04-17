def dfs(adj,o):
    return dfs_aux(adj,o,set(),{})

def dfs_aux(adj,o,vis,pai):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            pai[d] = o
            dfs_aux(adj,d,vis,pai)
    return vis

def maior(vizinhos):
    
    def make_grafo(vizinhos, grafo):
        for fronteiras in vizinhos:
            lista_aux = []
            for pais in fronteiras:
                if pais not in grafo:
                    grafo[pais] = []
                
                lista_aux.append(pais)
                if pais not in paises:
                    paises.append(pais)
            for pais in fronteiras:
                for i in range(len(lista_aux)):
                    if lista_aux[i] != pais:
                        grafo[pais].append(lista_aux[i])     
                
    grafo={}   
    paises=[]
    maior = 0
    make_grafo(vizinhos, grafo)
    
    for pais in paises:
        resp = (len(dfs(grafo,pais)))
        if resp > maior:
            maior = resp
    
    return maior

# 100 %