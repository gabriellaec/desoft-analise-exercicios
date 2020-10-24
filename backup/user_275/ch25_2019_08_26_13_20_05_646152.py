distância=float(input("qual eh a distância:"))   
if distância>200:
    total=200*0.50+(distância-200)*0.45
else:
    total=distância*0.5
print("{0:.2}".format(total))  