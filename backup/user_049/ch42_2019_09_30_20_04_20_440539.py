n=input("Número: ")

def quantos_uns(n):
    i=0
    uns=0
    while i < len(n):
        if n[i] == '1':
            uns+=1
            i+=1
        else:
            i+=1
    return uns