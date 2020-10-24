cig = int(input("Quantidade de cigarros: "))        
a = int(input("Quantidade de ano: "))

def temp_perd(cigarro,anos):
    y = (cigarro*10)/(60/24)/365*(anos)
    return y

total = temp_perd(cig,a)

print("Total de anos perdidos foi:{0} ".format(total))
    
    