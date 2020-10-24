def acha_bigramas(string):
    l= []
    for i in range(2, len(string)+1):
        x= string[i-2:i] #string[i-2:i-1]
        if x not in l:
            l.append(x)
    return l