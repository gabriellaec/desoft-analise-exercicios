
cig = int(input("Quantos cigarros vc fuma? "))
temp = int(input("A quanto tempo vc fuma? "))
def tempo_perdido(cig,temp):
    y= temp/365 + cig*1/6*1/24
    return y
       