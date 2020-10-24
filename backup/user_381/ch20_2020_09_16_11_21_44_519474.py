x = int(input('Qual a distância que você deseja percorrer?'))
if x <= 200:
    y = x*(0.50)
elif x > 200:
    y = x*(0.45) + 100
print('O preço é {0:.2f}'.format(y))

                    
    
                  
             