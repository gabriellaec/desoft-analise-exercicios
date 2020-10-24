def calcula_tempo(dict):
    dict2 = {}
    for i in dict:
        dict2[i] = (dict[i]*200)**(1/2)
    return dict2