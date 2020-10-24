def remove_vogais (str):
    v= ["a","e","i","o","u"]
    l=[]
    for i in str:
        if i not in v:
            l.append(i)
    
    return l