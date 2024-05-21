def complete(dic_fellas, candidate, memo):
    for i in range(len(candidate) - 1):
        for j in range(i + 1, len(candidate)):
            if (candidate[i] not in dic_fellas[candidate[j]] or candidate[j] not in dic_fellas[candidate[i]]):
                return False
    memo[len(candidate)] = candidate
    return True

def extensions(candidate):
    ext = []
    for person in candidate:
        cpy_candidate = candidate.copy()
        cpy_candidate.remove(person)
        ext.append(cpy_candidate)
    return ext      

def search(dic_fellas, candidate, memo):
    if(len(candidate) in memo):
        return len(candidate)
    if complete(dic_fellas, candidate, memo):
        return len(candidate)
    for nxtcandidate in extensions(candidate):
        search(dic_fellas, nxtcandidate, memo)
    return max(memo.keys())

def amigos(conhecidos):
    if not conhecidos:
        return 0
    dic_fellas = {}
    for par in conhecidos:
        if par[0] not in dic_fellas:
            dic_fellas[par[0]] = []
        if par[1] not in dic_fellas:
            dic_fellas[par[1]] = []
        dic_fellas[par[1]].append(par[0])
        dic_fellas[par[0]].append(par[1])

    return search(dic_fellas, [x for x in dic_fellas], {})

# 80 % (penso que o algoritmo esteja certo mas não é o mais eficiente)