def cigarro_mata(anos,cig):
    y=(anos*365*cig*(10/1440))
    return y 

cig = int(input("quantos cigarros vc fuma: "))
anos= int(input("qtos anos vc fuma: "))
print (cigarro_mata(anos,cig))