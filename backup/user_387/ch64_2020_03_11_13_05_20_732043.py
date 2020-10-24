def acha_bigramas(a):
    p=[]
    for ele in range(len(a)):
        if len((a[ele:(ele+2)])) == 2:
            if (a[ele:(ele+2)]) not in p:
                p.append(a[ele:(ele+2)])

    return p
        
        