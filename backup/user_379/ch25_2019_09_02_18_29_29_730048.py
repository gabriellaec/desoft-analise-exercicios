x=int(input("digite a km da sua passagem"))
if x<=200:
    print("o preço é {:2f} reais".format(x*0.5))
else:
    print("o preço é {:2f} reais".format(100+((x-200)*0.45)))