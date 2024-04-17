def aux(passos, probs, x, y, cache):
    if (passos,x,y) in cache:
        return cache[(passos,x,y)]
        
    if passos == 0 and x == 0 and y == 0:
        return 1
    elif passos == 0 and (x != 0 or y != 0):
        return 0
        
    n = probs['U'] * aux(passos - 1, probs, x, y+1, cache)
    s = probs['D'] * aux(passos - 1, probs, x, y-1, cache)
    e = probs['R'] * aux(passos - 1, probs, x+1, y, cache)
    o = probs['L'] * aux(passos - 1, probs, x-1, y, cache)
    
    cache[(passos,x,y)]=(n+s+e+o)
    return cache[(passos,x,y)]
    

def probabilidade(passos,probs):
    if passos % 2 != 0:
        return 0
    return round(aux(passos, probs, 0, 0, {}),2)


# 100 %