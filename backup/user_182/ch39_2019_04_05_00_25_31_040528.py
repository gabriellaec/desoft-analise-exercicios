a=int(input("me fale valores"))

def soma(a):
    s=0
    while a>=0:
        if a>0:
            s=s+a
            a=int(input("me fale valores"))
        else:
            return s

print(soma(a))