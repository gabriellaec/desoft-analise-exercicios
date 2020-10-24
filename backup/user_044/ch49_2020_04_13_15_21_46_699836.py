def inverte_lista(ls1):
    ls2=[]
    lengh=len(ls1)-1
    i=0
    while i<=len(ls1)-1:
        ls2.append(ls1[lengh])
        i+=1
        lengh-=1
    return ls2