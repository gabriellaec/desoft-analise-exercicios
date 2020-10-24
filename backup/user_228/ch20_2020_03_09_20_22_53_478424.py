d=float(input("distância em km"))
if d<=200:
    a=d*0.5
else:
    a=(d-200)*0.45+100
print("{0:.2f}".format(a))

