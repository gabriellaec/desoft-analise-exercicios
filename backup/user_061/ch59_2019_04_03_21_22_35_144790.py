def conta_a(string):
    conta = 0
    i = 0
    while i<len(string):
        if string[i] == "a":
            conta += 1
        i+=1
    return conta