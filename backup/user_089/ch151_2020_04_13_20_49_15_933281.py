def classifica_lista(x):
    resultado = []
    if x == [] or len(x) < 2:
        return "nenhum"  
    i = 0 
    while i < len(x):
        if x[i] > x[i+1]:
            i += 1
            resultado.append('d')

        if x[i] < x[i+1]:
            i += 1
            resultado.append("c") 
    
    if "d" and "c" in resultado:
        return "nenhum"
    if "d" not in resultado:
        return "crescente" 
    if "c" not in resultado:
        return "decrescente"