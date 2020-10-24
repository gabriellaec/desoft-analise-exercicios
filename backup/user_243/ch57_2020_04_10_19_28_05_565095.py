def verifica_progressao(lista):
    i=1
    while i<len(lista):
        if lista[i+1]/lista[i]==lista[i]/lista[i-1]:
            print ("PG")
        elif lista[i+1]-lista[i]==lista[i]-lista[i-1]:
            print ("PA")
        elif lista[i+1]/lista[i]==lista[i+1]-lista[i]:
            print("AG")
        else:
            print("NA")
        i+=1
        