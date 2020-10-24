def quantos_uns(numero):
    numero=str(numero)
    i=0
    quantidade=0
    while True:
        if i==len(numero):
            break
        elif numero[i]== '1':
            quantidade+=1 
        elif numero[i]!='1':
            quantidade+=0
        i+=1
        
    return quantidade