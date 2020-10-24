x=True
while x==True:
    resp = input ("Vc possui alguma dúvida?: ")
    if resp != "não":
        print ("Pratique mais")
    elif resp == "não":
        print ("Até a próxima")
        x = False