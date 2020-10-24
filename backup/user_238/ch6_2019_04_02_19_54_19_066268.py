def encontra_maximo(matriz):
    maior=matriz[0][0]
    i=0
    a=0
    while a<3: 
            if matriz[a][i]>maior:
              	maior=matriz[a][i]
            if i== 2 or i==5 or i==8:
            	a+=1
                i=0
        	i+=1
    return maior
matriz=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(encontra_maximo(matriz))