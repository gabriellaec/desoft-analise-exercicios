def acha_bigramas(palavra):
    listabi=[]
    i=0
    while i<(len(palavra)-1):
        bi=palavra[i]+palavra[i+1]
        if bi in listabi:
            listabi=listabi
        else:
            listabi.append(bi)
        i=i+1
    return listabi