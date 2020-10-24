leo = float(input ("Qual a distância que deseja percorrer?"))     
if leo<= 200:
    a= (leo*0.5)
else:
    a= ((leo-200)*0.45+100)
print ("{0:.2f}".format(a))