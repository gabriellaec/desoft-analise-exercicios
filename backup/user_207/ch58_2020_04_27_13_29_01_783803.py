def conta_a (palavra):
    i =0
    count = 0
    while i< len(palavra):
        if palavra[i] == 'a':
            count +=1
        i +=1
    return count
