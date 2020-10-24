def classifica_lista(num):
    if len(num)<2:
        return "nenhum"
    else:
        i=0
        while i<len(num)-1:
            if num[i]<num[i+1]:
                crescente=True
                i=i+1
            else:
                crescente=False
                j=0
                while j<len(num)-1:
                    if num[j]>num[j+1]
                        decrescente=True
                        j=j+1
                    else:
                        decrescente=False
                        nenhum=True
    if crescente==True:
        return "crescente"
    elif descrescente==True:
        return "decrescente"
    else:
        return "nenhum"

