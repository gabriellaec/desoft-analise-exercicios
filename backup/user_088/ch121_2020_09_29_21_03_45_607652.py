def subtracao_de_listas(l1,l2):
    i=0
    j=0
    while(i<len(l1) and j<len(l2)):
        if(l1[i]==l2[j]):
            del l1[i]
        i+=1
        j+=1
        print(l1)
         