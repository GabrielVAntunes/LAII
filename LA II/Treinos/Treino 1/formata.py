def formata(codigo):

    codigo_ident = ""
    special_chars = [";", "{", "}"]
    num_espacos=0
    i=0

    codigo = list(codigo)
    codigo.append("@")

    for i in range(len(codigo)):
        if codigo[i-1] in special_chars:
            while codigo[i] == " ":
                codigo[i] = ""
                i+=1

    for i in range(len(codigo)-1):
        
        if codigo[i+1] != "@":
            if codigo[i] not in special_chars:
                codigo_ident += codigo[i]
            elif codigo[i] == ";":
                codigo_ident += codigo[i]
                codigo_ident += "\n" 
                if codigo[i+1] != "}":
                    codigo_ident += "  " * num_espacos
            elif codigo[i] == "{":
                codigo_ident += codigo[i]
                num_espacos +=1
                codigo_ident += "\n" 
                if codigo[i+1] != "}": 
                    codigo_ident += "  " * num_espacos
            else:
                codigo_ident += codigo[i]
                num_espacos -=1
        else:
            codigo_ident += codigo[i]
    return codigo_ident

# 40 % 