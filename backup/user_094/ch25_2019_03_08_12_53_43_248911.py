d = float(input("Que distância, em km, você quer percorrer?"))
preco=0              
if d>200:
    preco = (d-200)*0.45 + 200*0.50
    print ("{:12.2f}".format(preco))
else:
    preco= (d*0.50)
    print ("{:12.2f}".format(preco))
   

