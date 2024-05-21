import math

def sacos(peso,compras):
    if not compras: 
        return 0
    return math.ceil(sum(compras)/peso)

# 80 % (resolução claramente preguiçosa)