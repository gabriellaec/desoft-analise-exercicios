vel=int(input("qual a vel maxima?  "))
dist=int(input("qual a distancia?  "))

running=True


while running:
    placa=input("qual a placa  ")
    instante1=input("qual o primeiro instante  ")
    instante2=input("qual o segundo instante  ")
    
    inst1=int(instante1)
    inst2=int(instante2)
    if placa == 0:
        
        running = False
    
    
    if running == True:
        inst_total= inst2 - inst1
        
        vel_total=dist/inst_total
        vel1=vel*1.2
        vel2=vel*1.5
        
        if vel_total <= vel:
            print('vc ta de boa',placa)
        elif vel_total > vel and vel_total <= vel1:
            print('sua multa foi media:130R$',placa)
        elif vel_total > vel1 and vel_total <= vel2:
            print('sua multa foi grave:193R$',placa)
        else:
            print('sua multa foi gravissima:3X195R$',placa)
            
    
        
    else:
        running=False