contador=0
with open ("macacos-me-mordam.txt", "r") as arq:
    a= arq.read()
    c=a.lower()
    b=c.split()
    for i in b:
        if i == "banana":
            contador+=1
print contador
            