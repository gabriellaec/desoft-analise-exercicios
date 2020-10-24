def eh_crescente(l1):
    if len(l1)<2:
        return False
    for i in range (len(l1)-1):
        if l1[i] >= l1[i+1]:
            return False
    return True
    
def eh_decrescente(l2):
    if len(l2)<2:
        return False
    for i in range (len(l2)-1):
        if l2[i] <= l2[i+1]:
            return False
    return True
    
def classifica_lista(l3):
    if eh_crescente (l3) == True:
        return "crescente"
    elif eh_decrescente (l3) == True:
        return "decrescente"
    else:
        return "nenhum"