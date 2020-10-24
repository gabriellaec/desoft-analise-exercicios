def junta_nome_sobrenome(name, family):
    n = len(name)
    i=0
    new=[]
    
    while i < n:
        a=name[i]
        b=family[i]
        new.append(a+" " +b)
        i=i+1
    return new