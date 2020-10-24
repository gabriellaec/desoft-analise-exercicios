def equaliza_imagem(list,k):
    i=0
    new_list = list
    X = len(list)
    while i <= X:
        new_list[i] = list[i]*k
        if new_list[i] > 255:
            new_list[i] = 255
        i=i+1
    return new_list
    