def equaliza_imagem(pixel,k):
    n = len(pixel)
    i=1
    if n < 0:
        if pixel[0]*k > 255:
            l=[255]
        else:
            l=[pixel[0]*k]
    
    while i < n:
        if pixel[i]*k > 255:
            l.append(255)
        else:
            l.append(pixel[i]*k)
        i=i+1
            
    return l