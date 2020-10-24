def login_disponivel(s, lista):
    string = ""
    cont = 0
    if lista == []:
        return s
    for i in lista:
        if s in lista:
            if i == s + str(string) or i == s + str(cont):
                cont = cont + 1
        else:
            return s
    return s + str(cont)

l= []
while True:
    s = input("Qual o usuário? ")
    if s == "fim":
        break
    a= login_disponivel(s, l)
    l.append(a)
    
for i in l:
    print(i)
    