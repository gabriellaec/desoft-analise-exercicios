def segundos_entre(x,y):
    X = x.replace(':','')
    Y = y.replace(':','')
    Lx = []
    Ly = []
    resposta = 0
    i=0
    for e1,e2 in zip(X,Y):
        Lx.append(float(e1))
        Ly.append(float(e2))
    
    while i < len(Lx)-5:    
        resposta_h = ((Ly[i]+Ly[i+1])-(Lx[i]+Ly[i+1]))*3600
        resposta_m = ((Ly[i+2]+Ly[i+3])-(Lx[2+i]+Ly[i+3]))*60
        resposta_s = ((Ly[i+4]+Ly[i+5])-(Lx[i+4]+Lx[i+5]))
        i+=1
    resposta += resposta_h+resposta_m+resposta_s             
    return resposta
        
    
    
    