a=input("fala um email ai: ")

def pos_arroba(x):
    i=0
    while x[i]!= "@":
        i+=1
    return i+1

print(pos_arromba(a))

