dic={'a':1,'b':2,'c':3,'d':'r','r':3, 'd':5}
def bloop(dic):
    lista=[]
    
    for i in dic:
        if i not in lista:
            lista.append(i)
    return lista
print(bloop(dic))
