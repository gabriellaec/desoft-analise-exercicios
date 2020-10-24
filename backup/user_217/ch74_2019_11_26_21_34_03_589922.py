def conta_bigramas(string):
    string=[]
    dicionario={}
    for i in range(len(string)-1):
        bigrama=(string[i],string[i+1])
        if bigrama not in dicionario:
            dicionario[bigrama] = 0
        dicionario[bigrama]+=1
        
    bigrama_freq_1 = 0
    bigrama_freq_2 = 0
    for brigrama in dicionario:
        if dicionario[bigrama] ==1:
            bigrama_freq_1+=1
        elif dicionario[bigrama] ==2:
            bigrama_freq_2+=1
            
    return dicionario