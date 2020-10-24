def verifica_progressao(lista):
    i=1
    while i<len(lista):
        if lista[i+1]/lista[i]==lista[i]/lista[i-1]:
            print ("PG")
        if lista[i+1]-lista[i]==lista[i]-lista[i-1]:
            print ("PA")
        if lista[i+1]/lista[i]==lista[i+1]-lista[i]:
            print("AG")
        else:
            print("NA")
        i+=1
        