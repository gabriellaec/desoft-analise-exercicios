def eh_crescente(l1):
    if l1 == [] or len(l1) == 1:
        return "nenhum"
    else:
        for i in range (len(l1)-1):
            if l1[i+1] <= l1[i]:
                return False
        return True
    
def eh_decrescente(l2):
    if l2 == [] or len(l2) == 1:
        return "nenhum"
    else:
        for i in range (len(l2)-1):
            if l2[i+1] >= l2[i]:
                return False
        return True
    
def classifica_lista(l1):
    if eh_crescente (l1) == True:
        return "crescente"
    elif eh_descrecente (l1) == True:
        return "decrescente"
    elif len(l1)<2:
        return "nenhum"
    else:
        return "nenhum"