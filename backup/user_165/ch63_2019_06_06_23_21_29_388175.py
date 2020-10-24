a=input("Digite um email: ")
def pos_arroba(email):
    i=0
    while email[i]!= "@":
        i+=1
    return i
print(pos_arroba(a))
