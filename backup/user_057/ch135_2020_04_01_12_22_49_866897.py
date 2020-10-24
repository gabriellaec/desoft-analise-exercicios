def equaliza_imagem(list,k):
    i=0
    new_list = list
    while i <= len(list):
        new_list[i] = list[i]*k
        if new_list[i] > 255:
            new_list[i] = 255
    return new_list
    