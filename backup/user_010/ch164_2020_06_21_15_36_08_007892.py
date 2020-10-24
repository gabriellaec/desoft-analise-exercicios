def traduz (ingles,dic):
    portugues=[]
    for ing in ingles:
        for i,p in dic.items():
            if i==ing:
                portugues.append (p)
    return portugues