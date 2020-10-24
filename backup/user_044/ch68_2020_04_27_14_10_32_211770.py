def separa_trios(ls1):
    ls2=[]
    i=0
    while i!=len((ls1)):
        ls2.append(','.join(ls1[i:i+3]))
        i+=3