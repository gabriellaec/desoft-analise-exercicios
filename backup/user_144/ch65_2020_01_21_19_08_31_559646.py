def acha_bigramas(words):
 
    bigrams = []
 
    for i in range(0, len(words)):
        if (i == len(words)-1):
            break
        else:
            bigrama_obs = words[i] + words[i+1]
            if bigrama_obs not in bigrams:
                bigrams.append(bigrama_obs)
 
    return bigrams
