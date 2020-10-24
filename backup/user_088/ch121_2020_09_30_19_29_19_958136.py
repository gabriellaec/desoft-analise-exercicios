def subtracao_de_listas(l1,l2):
    i=0
    j=0
    while(i<len(l1)): 
        while( j<len(l2)):
               if(l1[i]==l2[j]):
                    del l1[i]
                    j+=1
                i+=1
    return l1
         