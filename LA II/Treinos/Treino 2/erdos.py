def bfs(adj):
    erdos = {"Paul Erdos": 0}
    queue = ["Paul Erdos"]
    while queue:
        v = queue.pop(0)
        for d in adj:
            if v in adj[d]:
                for autor in adj[d]:
                    if autor not in erdos:
                        erdos[autor] = erdos[v] + 1
                        queue.append(autor)
    return erdos

def erdos(artigos,n):
    
    erdos = bfs(artigos)
    
    lista_erdos = []
    resp = []

    for autor in erdos:
        if erdos[autor] <= n:
            lista_erdos.append((autor, erdos[autor]))

    lista_erdos.sort(key = lambda t: t[0])
    lista_erdos.sort(key = lambda t: t[1])

    for par in lista_erdos:
        resp.append(par[0])

    return resp

# 100 %