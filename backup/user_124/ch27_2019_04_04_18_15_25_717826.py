
cig = int(input("Quantos cigarros vc fuma? "))
temp = int(input("A quanto tempo vc fuma? "))
def tempo_perdido(cig,temp):
    y= temp*cig
    z= y*10/60*1/24
    return z
print(tempo_perdido(cig,temp))
       