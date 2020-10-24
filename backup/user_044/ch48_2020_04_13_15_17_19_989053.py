def estritamente_crescente(lista):
    ls=[]
    m=0
    for i in lista:
        if len(ls)!=0:
            m=max(ls)
        if i>m:
            ls.append(i)
    return ls           
def eh_crescente(ls1):
    if len(ls1)==len(estritamente_crescente(ls1)):
        return True
    else:
        return False