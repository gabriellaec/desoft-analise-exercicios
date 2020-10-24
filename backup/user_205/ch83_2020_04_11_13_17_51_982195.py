def medias_por_inicial(dic):
    resultado = {}
    soma = 0
    for chaves,valores in dic.items():
        for i in range(len(chaves)-1):
            if chaves[i] == chaves[i+1]:
                resultado[chaves[i]]=valores[i]+valores[i+1]/2
                break
            else: 
                resultado[chaves[i]]=valores
                break
                
    print (resultado)
    return resultado

            