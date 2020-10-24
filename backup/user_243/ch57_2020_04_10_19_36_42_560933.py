def verifica_progressao(lista):
    i=0
    while i<len(lista):
        if lista[i+2]/lista[i+1]==lista[i+1]/lista[i]:
            print ("PG")
        if lista[i+2]-lista[i+1]==lista[i+1]-lista[i]:
            print ("PA")
        if lista[i+2]/lista[i+1]==lista[i+2]-lista[i+1]:
            print("AG")
        else:
            print("NA")
        i+=1
        