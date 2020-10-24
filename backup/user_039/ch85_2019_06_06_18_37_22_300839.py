contador=0
with open ("macacos-me-mordam.txt", "r") as arq:
    a= arq.read()
    c=a.lower()
    c=c.split()
    for i in c:
        if i == "banana":
            contador+=1
    return contador
            