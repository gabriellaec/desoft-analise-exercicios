resp = input ("Vc possui alguma dúvida?: ")
while resp!="não":
    resp2 = input ("Vc possui alguma dúvida?: ")
    if resp2 != "não":
        print ("Pratique mais")
    elif resp2 == "não":
        print ("Até a próxima")