def conta_bigramas(x):
    string='babana nanica'
    dicionario={}
    for i in range(len(string)):
        bigrama=(string[i:i+2])
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