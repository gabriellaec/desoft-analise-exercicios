dist = int(input("insira a quantidade de km que deseja percorrer: "))
if 0 <= dist <= 200:
    price = dist * 0.5
    print ('R${0:.2f}' .format(price))
elif dist>200:
    price = (dist - 200)*0.45 + 200*0.5
    print('R${0:.2f}' .format(price))