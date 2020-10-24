def segundos_entre(horario1, horario2):
    total=0
    total1=0
    total2=0
    
    primeiro1=0
    segundo1=0
    terceiro1=0
    quarto1=0
    quinto1=0
    sexto1=0
    
    primeiro2=0
    segundo2=0
    terceiro2=0
    quarto2=0
    quinto2=0
    sexto2=0
    
    primeiro1 = int(horario1[0])
    primeiro1 = primeiro1*10*3600
    
    segundo1 = int(horario1[1])
    segundo1 = segundo1*3600
    
    terceiro1 = int(horario1[3])
    terceiro1 = terceiro1*10*60
    
    quarto1 = int(horario1[4])
    quarto1 = quarto1*60
    
    quinto1 = int(horario1[6])
    quinto1 = quinto1*10
    
    sexto1 = int(horario1[7])
    sexto1 = sexto1
    
    total1=primeiro1+segundo1+terceiro1+quarto1+quinto1+sexto1
    
    
    primeiro2 = int(horario2[0])
    primeiro2 = primeiro2*10*3600
    
    segundo2 = int(horario2[1])
    segundo2 = segundo2*3600
    
    terceiro2 = int(horario2[3])
    terceiro2 = terceiro2*10*60
    
    quarto2 = int(horario2[4])
    quarto2 = quarto2*60
    
    quinto2 = int(horario2[6])
    quinto2 = quinto2*10
    
    sexto2 = int(horario2[7])
    sexto2 = sexto2
    
    total2=primeiro2+segundo2+terceiro2+quarto2+quinto2+sexto2
    
    total=total2-total1
    return total