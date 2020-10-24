duvida= True
a= input("tem duvida(sim/não)? ")
if a == "não":
    duvida= False
    print ("Até a próxima")
while duvida==True:
    print ("Pratique mais")
    a= input("tem duvida(sim/não)? ")
    if a == "não":
        duvida= False
        print ("Até a próxima")
    
    