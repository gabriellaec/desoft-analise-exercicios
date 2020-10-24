def eh_crescente(lista):
        i=0
        contador=0
        if (len(lista)<2):
            return True
        while (i <(len(lista) - 1)):
            if (lista[i+1] > lista[i]):
                contador+=1
            i+=1
         if(contador==len(lista)-1):
            return True
         else:
             return False  