def login_disponivel(nome,lista):
    if nome not in lista:
        return nome
    else:
        i=1
        k=list(nome)
        while i<len(k):
            k.append(i)
            m="".join(k)
            if m not in lista:
                return m
            else:
                i+=1
            
            
        
        
        
        
        

        
        