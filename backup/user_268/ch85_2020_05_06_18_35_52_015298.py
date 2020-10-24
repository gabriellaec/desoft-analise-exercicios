with open("macacos-me-mordam.txt", "r") as arq:
    cont = arq.read()
    lc = cont.lower()
    sp = lc.split()
    a = 0
    for i in sp:
        if i == "banana":
            a+=1
return a