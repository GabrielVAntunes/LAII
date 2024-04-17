def aux(mapa, x, y, xfinal, yfinal, cache):
    if x == xfinal and y == yfinal:
        if mapa[x][y] not in [".","#"]:
            return int(mapa[x][y])
        else:
            return 0

    if (x,y) in cache:
        return cache[(x,y)]

    b = 0
    d = 0

    if x + 1 <= xfinal and mapa[x+1][y] != "#":
        if mapa[x][y] == ".":
            d = 0 + aux(mapa, x+1, y, xfinal, yfinal, cache)
        else:
            d = int(mapa[x][y]) + aux(mapa, x+1, y, xfinal, yfinal, cache)
    if y + 1 <= yfinal and mapa[x][y+1] != "#":
        if mapa[x][y] == ".":
            b = 0 + aux(mapa, x, y+1, xfinal, yfinal, cache)
        else:
            b = int(mapa[x][y]) + aux(mapa, x, y+1, xfinal, yfinal, cache)
    
    cache[(x,y)] = max(b,d)
    return cache[(x,y)]

def saque(mapa):
    return aux(mapa, 0, 0, len(mapa) - 1, len(mapa[0]) - 1, {})

# 80 %