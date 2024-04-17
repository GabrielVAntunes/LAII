def frequencia(texto):
    palavras = texto.split()
    palavras.sort()
    resp = []

    for palavra in palavras:
        if palavra not in resp:
            resp.append(palavra)
    
    resp.sort(key = lambda palavra: palavras.count(palavra), reverse=True)

    return resp

# 100 %