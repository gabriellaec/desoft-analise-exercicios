def segundos_entre(primeiro_horario, segundo_horario):
    
    primeiro_horario=input('Digite um horario, com 4 digitos: ')
    segundo_horario=input('Digite um segundo horario, com 4 digitos: ')
    
    a= len(primeiro_horario)
    b= len(segundo_horario)
    if a>5:
        print('Horario inválido')
    if b>5:
        print('Horario inválido')
        
    hora_1= primeiro_horario[:2]
    min_1= primeiro_horario[2:4]
    seg_1= primeiro_horario[4:6]
    hora_2= segundo_horario[:2]
    min_2= segundo_horario[2:4]
    seg_2= segundo_horario[4:6]
    
    int(hora_1)
    int(min_1)
    int(seg_1)
    int(hora_2)
    int(min_2)
    int(seg_2)
    
    dif_hora= (int(hora_1) - int(hora_2))
    dif_minuto= (int(min_1) - int(min_2))
    dif_seg= (int(seg_1) - int(seg_2))
    
    print(dif_hora , ':' , dif_minuto , ':' , dif_seg)