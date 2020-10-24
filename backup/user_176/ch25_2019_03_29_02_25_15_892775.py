d= int(input('qual a distancia que deseja percorrer?'))
if d <= 200:
    print (d*0.50)
elif d > 200:
    print (100 + (d-200)*0.45)
    
