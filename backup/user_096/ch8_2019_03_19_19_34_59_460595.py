
import math
def verifica_progressao(lista):
    i=0
    while i<len(lista):
        if (lista[i]+lista[i+2])/2==lista[i+1]:
            return"PA"
            print("PA")
        elif (math.sqrt(lista[i]+lista[i+2]))==lista[i+1]:
            return"PG"
            print("PG")
        elif (lista[i]+lista[i+2])/2==lista[i+1] and (math.sqrt(lista[i]+lista[i+2]))==lista[i+1]:
            return"AG"
            print("AG")
        else:
            return"NA"
            print("NA")
