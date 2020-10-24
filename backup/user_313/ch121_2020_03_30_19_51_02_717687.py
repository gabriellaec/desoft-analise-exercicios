l3 = []

def subtracao_de_listas(l1,l2):
    contador1 = 0
    contador2 = 0
    aparece = False

    while contador1 < len(l1):
        #if l1[contador1]
        
        while contador2 < len(l2):
            if l1[contador1] == l2[contador2]:
                aparece = True
            contador2 += 1

        if aparece == False:
            l3.append(l1[contador1])
    
        contador1 += 1

    return l3