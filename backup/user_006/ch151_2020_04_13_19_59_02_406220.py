def classifica_lista(num):
    crescente=False
    decrescente=False
    nenhum=False
    if len(num)<2:
        nenhum=True
    else:
        i=0
        while i<len(num)-1:
            if num[i]<num[i+1]:
                crescente=True
                i=i+1
            else:
                crescente=False
                i=len(num)-1
        j=0
        while j<len(num)-1:
            if num[j]>num[j+1]:
                decrescente=True
                j=j+1
            else:
                decrescente=False
                nenhum=True
                j=len(num)-1
                        
    if crescente==True:
        return "crescente"
    elif decrescente==True:
        return "decrescente"
    else:
        return "nenhum"

