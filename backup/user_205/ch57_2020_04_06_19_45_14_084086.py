def verifica_progressao(lista):
        lista_final = []
        i = 0
        while i<len(lista)-2:
            if (lista[i+2] == (lista[i]+lista[i+1])/2):
                lista.append("PA")   
            elif (lista[i+1]**2==lista[i]*lista[i+2]):
                lista.append("PG")
            elif (lista[i+2] == (lista[i]+lista[i+1])/2) and (lista[i+1]**2==lista[i]*lista[i+2]):
                lista.append("AG")
            else:
                lista.append("NA")
            i+=1
        return lista_final[0]
        
