def calucla_tempo0(a):
    t = (200*a)**(1/2)
    return t

def calcula_tempo(dict):
    dict2 = {}
    for i in dict:
        dict2[i] = calcula_tempo0(dict[i])
    return dict2