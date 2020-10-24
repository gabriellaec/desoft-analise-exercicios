def lista_sufixos(string):
    bigrams = []
 
    for i in range(0, len(words)):
        if (i == len(words)-1):
            break
        else:
            bigrama_obs =words[-3]+words[-2]+words[-1]
         
            if bigrama_obs not in bigrams:
                bigrams.append(bigrama_obs)
 
    return bigrams