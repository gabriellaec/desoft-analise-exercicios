a=input("Digite um email: ")
def pos_arroba(email):
    i=0
    while email[i]!= "@":
        i+=1
    return i+1
print(pos_arroba(a))
