def conta_bigramas(palavra):
    dict = {}
    for i in range(len(palavra)-1):
        big = palavra[i:i+2]
        if big not in dict:
            dict[big] = 1
        else: dict[big] += 1
            
    return dict