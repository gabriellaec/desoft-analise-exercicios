duvida= True
a= input("tem duvida(sim/não)? ")
if a == "não":
    duvida= False
    print ("Até a proxima")
while duvida==True:
    print ("Pratique mais")
    a= input("tem duvida(sim/não)? ")
    if a == "não":
        duvida= False
        print ("Até a proxima")
    
    