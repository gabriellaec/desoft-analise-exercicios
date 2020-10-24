lista1=['beto','caio','rod']
def login_disponivel(lista1):
    s=0  
    lista=[]
    for i in lista1:
        log=str(input('digite seu login: '))
        if log =='fim':
            break
        elif log in lista1:   
            s+=1
            n='{0}{1}'.format(log,s)
            lista.append(n)
            
        elif log not in lista1:
            lista.append(log)
    return lista

    
print(login_disponivel(lista1))