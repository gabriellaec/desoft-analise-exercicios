from math import sqrt
def calcula_tempo(dic):
    new_dic = {}
    for i in dic:
        v = sqrt(2*100*dic[i])
        t = v / dic[i]
        if t not in new_dic:
            new_dic[i] = t
            
    return new_dic
            
            
        
    