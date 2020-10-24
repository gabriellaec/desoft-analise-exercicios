def calcula_tempo(dict):
    dict2 = {}
    for i in dict:
        dict2[i] = (200/dict[i])**(1/2)
    return dict2