def capitaliza(palavra):
    cont=0
    while cont<len(palavra):
        capitalizada=palavra[0].upper() + palavra[1:cont+1]
        cont+=1
    return capitalizada

