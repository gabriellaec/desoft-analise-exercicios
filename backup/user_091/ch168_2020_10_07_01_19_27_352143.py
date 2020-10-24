def login_disponivel(nome,lista):
    if nome not in lista:
        return nome
    else:
        i=1
        k=list(nome)
        while i<len(k):
            k.append('{0}'.format(i))
            m="".join(k)
            if m not in lista:
                return m
            else:
                p=0
                g=list(m)
                while p<len(g):
                    g[len(g)-1]='{0}'.format(p-2)
                    l="".join(g)
                    p+=1
                i+=1
                return l
            
        
        
        
        
        

        
        