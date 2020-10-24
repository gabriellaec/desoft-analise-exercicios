def subtracao_de_listas(l1, l2):
    l3 = []
    l1_counter = 0
    while l1_counter < len(l1):
        l2_counter=0
        aparece = False
        while l2_counter <len(l2):
            if l1[l1_counter]==l2[l2_counter]:
                aparece = True
            l2_counter =+1
        if aparece == False:
        l2.append(l1[l1_counter])
        l1_counter +=1
        return l3           