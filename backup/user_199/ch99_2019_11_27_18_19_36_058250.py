log='beto'
lista=['beto','caio','rod','beto']
def login_disponivel(lista,log):
    s=0  
    for i in lista:
        if log in lista:   
            s+=1
            print(s)
            return '{0}{1}'.format(log,s)
        
        elif log not in lista:
            return log
    
print(login_disponivel(lista,log))