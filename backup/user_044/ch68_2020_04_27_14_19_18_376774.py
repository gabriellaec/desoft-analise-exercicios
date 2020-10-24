def separa_trios(ls1):
    ls2=[]
    if len(ls1)==1:
        ls2=ls1
    else:
        for i in range(0,len(ls1),3):
            ls2.append(','.join(ls1[i:i+3]))
    return ls2