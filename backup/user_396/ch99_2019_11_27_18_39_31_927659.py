x =['andre', 'fabio', 'lucio', 'lucio1']
nome = input("Qual é o seu nome? ")
def login_disponivel(x, nome):
    #s = 0
    i = 0
    while i < len(x):
        if nome in x:
            print("nome indisponivel")
        else:
            print("ok")
        i+=1
            
            
print(login_disponivel(x, nome))