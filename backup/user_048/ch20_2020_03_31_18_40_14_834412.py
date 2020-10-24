d=int(input("qual a distancia em km"))
if d<=200:
    y=d*0.5
else:
    y=(d-200)*0.45 + 200*0.5
print("%.2f" % y)