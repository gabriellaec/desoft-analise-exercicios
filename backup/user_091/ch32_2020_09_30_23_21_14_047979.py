def lista_primos(n):
        if n>=1:
            print (2)
            parametro1= 1
            parametro2= 3
            while parametro1<n:
                parametro3= 3
                while(parametro3<parametro2):
                    if parametro2 % parametro3==0:
                        break
                    parametro3+=2
                if parametro3==parametro2:
                    print (parametro3)
                    parametro1+=1
                parametro2+=2
            
    
    