def equaliza_imagem (l,k):
    l2=[0]*len(l)
    for p in range(len(l)):
        l2[p]=l[p] * k
        if l2[p] >255:
            l2[p]=255
    return l2      
          

       