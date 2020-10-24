def calcula_velocidade_media (si, sf, ti, tf):
    v=(sf-si)/(tf-ti)
    return v
x=int(input("Posição inicial:"))
y=int(input("Posição final:"))
w=int(input("Tempo inicial:"))
k=int(input("Tempo final:"))
z=calcula_velocidade_media (x, y, w, k)
print (z)