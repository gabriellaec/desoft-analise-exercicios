
def equaliza_imagem(l1,k):
    l2 = []
    i= 0 
    a = 0
    while i < len(l1):
        a = l1[i] * k 
        if a > 255:
            a = 255
        l2.append(a)
        i+=1
        a = 0
    return l2