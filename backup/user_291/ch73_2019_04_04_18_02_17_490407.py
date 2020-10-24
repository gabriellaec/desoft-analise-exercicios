def remove_vogais(palavra):
    lista = ["a", "e", "i", "o", "u"]
    
    i = 0
    
    while i < len(palavra):
        if palavra[i] in lista:
            vogal = palavra[:i+1]
            palavra1 = palavra[i+1:]
            semvogal = vogal[:i]
            palavra = semvogal+palavra1
        i += 1
        
    return palavra
            