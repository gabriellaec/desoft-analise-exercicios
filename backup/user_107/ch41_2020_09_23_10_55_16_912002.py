def zera_negativos (list):
    for i in range(0, len(list)):
        if list[i] < 0:
            list[i] = 0
            
    return list
