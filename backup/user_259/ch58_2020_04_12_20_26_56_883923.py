def conta_a(palavra):
    na = 0
    i = 0
    while i<len(palavra):
        if palavra[i] == 'a':
            na+=1
            i+=1
        else:
            i+=1
    return na    