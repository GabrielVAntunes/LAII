'''
Dada uma lista de strings com uma sopa de letras e
uma lista de palavras (uma matriz quadrada de 
caracteres), implemente uma função que
determine quantas dessas palavras aparecem na
sopa de letras. Uma palavra aparece na sopa de
letras se estiver escrita na horizontal ou na
vertical em qualquer das duas direcções.

input: palavras = ['age','mad','beg','god','dog','be','sad']
        matriz = ["cab",
                  "age",
                  "dog"]

output: 5

    input: palavras = ['is','so','no','in','on','si']
            matriz = ["sip",
                      "pic",
                      "not"]
    
    output: 4
'''

def get_vert(matriz, n):
    
    lista = []
    for i in range(n):
        wrd = ""
        for j in range(n):
            wrd += matriz[j][i]
        lista.append(wrd)
        
    for i in range(n):
        wrd = ""
        wrd2 = ""
        for j in range(n-1,-1,-1):
            wrd += matriz[j][i]
            wrd2 += matriz[i][j]
        lista.append(wrd)
        lista.append(wrd2)
    return lista
    
def sopa(matriz,palavras):
    
    verts = get_vert(matriz, len(matriz))
    check = []

    for palavra in palavras:
        for mat in matriz:
            if palavra in mat and palavra not in check:
                check.append(palavra)
        
        for vert in verts:
            if palavra in vert and palavra not in check:
                check.append(palavra)
    
    return len(check)
    
# 80 % 