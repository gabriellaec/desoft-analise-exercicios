dis = int(input("Distancia: "))

if dis <= 200:
    price = 0.5*dis
    print("Total: {:.2f}".format(price))

elif dis > 200:
    price1 = 200*0.5
    price2= (dis-200)*0.45
    total = price1 + price2
    print("Total: {:.2f}".format(total))