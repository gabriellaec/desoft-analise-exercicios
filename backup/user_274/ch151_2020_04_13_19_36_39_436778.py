def classifica_lista(list):
    if len(list) < 2:
        return "nenhum"
    n = len(list)
    i=1
    while i < n:
        if list[i-1] < list[i]:
            key = "c"
            i=i+1
        else:
            key = "n"
            break
    if key == "n":
        i=1
        while i < n:
            if list[i-1] > list[i]:
                key = "i"
                i=i+1
            else:
                key = "n"
                break       
    
    if key == "c":
        return "crescente"
    elif key == "i":
        return "decrescente"
    else:
        return "nenhum"