def lista_sufixos(palavra):
    i=0
    sufixo=[]
    while i<len(palavra)+1:
        if i==0:
            sufixo.append(palavra)
        else:
            sufixo.append(i)=palavra[i:(len(palavra))]
        i+=1
    return sufixo