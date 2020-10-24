with open ("macacos-me-mordam.txt", "r") as arq:
    a= arq.read()
    a=a.lower()
    a=a.split()
    for i in a:
        contador=0
        if i == "banana":
            contador+=1
    return contador
            