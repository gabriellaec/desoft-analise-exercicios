def equaliza_imagem(list,k):
    new_list = [i * k for i in list]
    i=0
    while i <= len(list):
        if new_list[i] > 255:
            new_list[i] = 255
    return new_list
    