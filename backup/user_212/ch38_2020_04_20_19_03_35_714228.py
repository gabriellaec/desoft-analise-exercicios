def quantos_uns (number):
    numero=str(number)
    i=0
    total=0
    while i<len(numero):
        if numero[i] == "1":
            total+=1
            i +=1
        if numero[i] != "1":
            total = total
            i+=1
    return total     
            