def conta_a(palavra):
    contador=0
    total  = 0
    
    while contador < len(palavra):
        if palavra[contador]=="a":
            total+=1
        contador+=1
           
    return total