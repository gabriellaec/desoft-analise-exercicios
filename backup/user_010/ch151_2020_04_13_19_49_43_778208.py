def classifica_lista(numeros):
    if len(numeros)<2:
        return "nenhum"
    else:
        crescente=0
        decrescente=0

        for i in range (len(numeros)-1):
            if numeros[i+1]>numeros[i]:
                crescente+=1

        for i in range (len(numeros)-1):
            if numeros[i+1]<numeros[i]:
                decrescente+=1


        if crescente==len(numeros)-1:
            return "crescente"
        elif decrescente==len(numeros)-1:
            return "decrescente"
        else:
            return "nenhum"