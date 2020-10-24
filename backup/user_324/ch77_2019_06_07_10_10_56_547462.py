import math
def calcula_tempo(dic):
    novodic={}
    listatletas=[]
    listatempo=[]
    for i in dic.keys():
        listatletas.append(i)
    for valores in dic.values():
        listatempo.append(math.sqrt(200/valores))
    for i in range(len(listatletas)):
        novodic[listatletas[i]]=listatempo[i]
    return novodic
        
        