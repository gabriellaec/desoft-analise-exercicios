def conta_a(palavra):
    num_a = 0
    for i in palavra:
        if 'a' == i:
            num_a+=1
        else:
            num_a = num_a
    return num_a
