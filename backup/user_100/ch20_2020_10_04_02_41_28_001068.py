
def f(d):  
      
    if d < 201:
        a = d*0.50
        return 'O valor é {0:.2f}'.format(a)
    
    else:
        g = 200 - d
        b = d*0.50 + g*0.45
        return 'O valor é {0:.2f}'.format(b)
    
t = float(input('Qual a distância que você deseja percorrer, em km?'))
print(f(t))
    