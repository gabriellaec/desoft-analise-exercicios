v_maxi = float(input("velocidade máxima: "))

v_max = v_maxi/3.6
print(v_max)

d_cam = float(input("distância entre as câmeras: ")) # em metros
t_cam1 = float(input("instante em que passa na primeira câmera: "))
t_cam2 = float(input("instante em que passa na segunda câmera: "))



dt = t_cam2 - t_cam1 #em segundos     
v = d_cam/dt


print(v)


while v > v_max:
    
    placa = str(input('placa do carro: '))
    if placa == ' ':
        break
    
    
    if v > v_max and v <= (0.2 * v_max)+v_max:
        p = 130.16
        print("Infração média. Penalidade: R${0}".format(p))
        break
        
        
    
    elif v > (0.2 * v_max)+v_max and v < (0.5 * v_max)+v_max:
        p = 195.23
        print("Infração grave. Penalidade: R${0}".format(p))
        break
        
    elif v > (0.5 * v_max)+v_max:
        p = 3 * 195.23
        print ("Infração gravíssima (suspensão imediata do direito de dirigir e apreensão do documento de habilitação). Penalidade: R${0}".format(p))
        break
    