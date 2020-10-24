perg = int(input ("Qual a distância de sua viagem?: "))

if perg<=200:
    custo = perg*0.5
    print("Sua passagem custa: ", custo) 
elif perg>200:
    #custo_extra = (perg-200)*0.45
    custo_normal = perg*0.45
    #custo_total = custo_normal + custo_extra
    
    print("Sua passagem custa: ", custo_normal)
    