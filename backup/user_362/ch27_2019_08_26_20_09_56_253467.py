def cigarros(cig,anos):
    rouba=(cig*10*365*anos)/1440
    return rouba
cig=int(input("quantos cigarros: "))
anos=int(input("quantos anos: "))
print(cigarros(cig,anos))