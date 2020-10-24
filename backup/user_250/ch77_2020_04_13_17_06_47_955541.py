def calculatempo(a):
    t = (200/a)**(1/2)
    return t

def calcula_tempo(dict):
    dict2 = {}
    for i in dict:
        dict2[i] = calculatempo(dict[i])
    return dict2