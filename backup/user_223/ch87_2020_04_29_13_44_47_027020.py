with open ('churras.txt', 'r') as churrastxt:
    linhas = churrastxt.readlines()
    print (linhas)
    custo = 0
    for linha in linhas:
        print (linha)
#        separa = linha.split(',')
 #       for e in separa:
  #          e1=float(e[1])
   #         e2=float(e[2])
    #        custo+=(e1*e2)
    #print (custo)