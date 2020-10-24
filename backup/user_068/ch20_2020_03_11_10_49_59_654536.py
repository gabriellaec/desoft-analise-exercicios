a = float(input("Qual distância que você deseja percorrer, em km? "))
if a <= 200:
           b = 0.50 * a
else:
           b = 0.50 * 200 + 0.45 * (a - 200)
print("{0:.2f}".format(b))
                
                
            
               
                