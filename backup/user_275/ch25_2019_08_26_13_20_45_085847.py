distância=float(input("qual eh a distância:"))   
if distância>200:
    total=100+(distância-200)*0.45
else:
    total=distância*0.5
print("{0:.2}".format(total))  