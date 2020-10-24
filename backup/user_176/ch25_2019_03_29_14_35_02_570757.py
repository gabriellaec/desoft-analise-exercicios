d= int(input('qual a distancia que deseja percorrer?'))
if d <= 200:
    print ("{0:.2f}".format(d*0.50))
else:
    print ("{0:.2f}".format(100 + (d-200)*0.45))
    
