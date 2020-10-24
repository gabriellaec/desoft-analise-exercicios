def eh_crescente(lista):
    if lista==[]:
        return True
    else:
        crescentes=[]
        crescentes.append(lista[0])
        for i in range(0,len(lista)-1):
            if lista[i+1]-lista[i]>0:
                crescentes.append(lista[i+1])
        if len(crescentes)==len(lista):
            return True
        else:
            return False