c = int(input("Quantos cigarros por dia?))
d = int(input("há quantos anos?))
           
def cigarritos(cigarros_dia, anos):  
    x = cigarros_dia*10*anos*365 /24 * 60
    return x
              
print ("você perdeu {0}.format(cigarritos(c,d)) 