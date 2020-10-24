distancia_percorer = input('Quandos Km você deseja percorrer?')
if distancia_percorer =< 200 : 
    print ('{0:.2f}'.format (distancia_percorer*(1/2)))
else:
    print  ('{0:.2f}'.format (distancia_percorer - (200*0.45)+100))