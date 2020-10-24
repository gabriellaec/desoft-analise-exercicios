def subtracao_de_listas(l1,l2):
    for item in l2:
        if item in l1:
            l1.remove(item)
        
    return l1