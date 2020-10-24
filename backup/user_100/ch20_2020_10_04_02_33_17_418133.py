d = float(input('Qual a distância que você deseja percorrer, em km?'))
def f(d):  
    
    
    if d < 201:
        a = d*0.50
        return a
    
    else:
        g = d - 200
        b = d*0.50 + g*0.45
        return b
    