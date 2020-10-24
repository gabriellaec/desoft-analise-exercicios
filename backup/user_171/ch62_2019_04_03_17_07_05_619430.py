def filtra_positivos (num):
    valores_pos = []
    i=0
    n=len(num)
    while i<n:
        if num[i]>0:
            valores_pos.append(num[i])
        i+=1
    return valores_pos
a=[-1,-3,4]
b= filtra_postivos(a)