""" moves:     0              
              |F|
           3     ) 1
          |E|     |D|
             ) 2 /
              |T|
"""

def robot(comandos):
    posicao_absoluta = 100
    coordenadas = [0 , 0]
    retangulos = []
    moves = ["F", "D", "T", "E"]
    maxx = 0
    maxy = 0
    minx = 0 
    miny = 0

    for comando in comandos:
        if (comando == "H"):
            coordenadas[0] = 0
            coordenadas[1] = 0
            retangulos.append((minx, miny, maxx, maxy))
            maxx = 0
            maxy = 0
            minx = 0 
            miny = 0
            posicao_absoluta = 100
        elif (comando == "E"):
            posicao_absoluta -= 1
        elif (comando == "D"):
            posicao_absoluta += 1
        else:

            if (moves[posicao_absoluta % 4] == "F"): 
                coordenadas[1] += 1
            elif (moves[posicao_absoluta % 4] == "E"):
                coordenadas[0] -= 1
            elif (moves[posicao_absoluta % 4] == "T"):
                coordenadas[1] -=1
            else:
                coordenadas[0] += 1

            print(coordenadas)
            print(posicao_absoluta)

            if(coordenadas[0] < minx):
                minx = coordenadas[0]
            elif (coordenadas[0] > maxx):
                maxx = coordenadas[0]
            elif (coordenadas[1] < miny):
                miny = coordenadas[1]
            elif (coordenadas[1] > maxy):
                maxy = coordenadas[1] 

    return retangulos

# 100 %