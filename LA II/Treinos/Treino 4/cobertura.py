def extensions(graph, candidate, nodes):
    valid_extensions = []
    for node in nodes:
        if node not in candidate:
            valid_extensions.append((node, graph[node]))

    # print("Valid" + str(valid_extensions))
    return valid_extensions

def valid(graph, candidate, nodes):

    verification_list = []
    
    for x in candidate:
        for y in graph[x]:
            verification_list.append(y)

    # print("verify " + str(verification_list))

    for node in nodes:
        if(node not in verification_list):
            # print("false")
            return False
    # print("true")
    # print(candidate)
    return True

def bigger(resp, candidate):
    if len(candidate) >= min(resp):
        return True
    return False

def search(graph, candidate, nodes, resp):
    # problably not needed
    #if complete(graph, candidate, nodes):
    if (candidate):
        if(resp and bigger(resp, candidate)):
            return resp
    if(valid(graph, candidate, nodes)):
        print("//////////////////////////////////////////////////////////////////////////")
        print(candidate)
        print("///////////////////////////////////////////////////////////////////////////")
        resp.append(len(candidate))
        return resp
    for key,value in extensions(graph, candidate, nodes):

        # print("aqui")
        # print(candidate)
        # print(key,value)
        new_candidate = candidate.copy()
        new_candidate[key] = value
        search(graph, new_candidate, nodes, resp)
    return resp

def mkgraph(arestas, graph):

    for aresta in arestas:
        if aresta[0] not in graph:
            graph[aresta[0]] = [aresta[0]]
        graph[aresta[0]].append(aresta[1])
        if aresta[1] not in graph:
            graph[aresta[1]] = [aresta[1]]
        graph[aresta[1]].append(aresta[0])
    return graph

def cobertura(arestas):
    graph = mkgraph(arestas, {})
    return min(search(graph, {}, [nodes for nodes in graph], []))
    

#print(cobertura([('a','b'),('b','c')]))
#print(cobertura([('a','b'),('b','c'),('c','d'),('d','e')]))
print(cobertura([('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','g'),('g','h')]))

# entendi mal o enunciado