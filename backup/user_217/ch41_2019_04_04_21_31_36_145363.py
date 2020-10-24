pergunta = True
while pergunta:
    a=input('Qual é a senha?:')
    
    if a == 'desisto':
        pergunta = False
        print('Você desistiu, a senha é Fernando') 
        
    if a != 'Fernando':
        
        print('Tente de novo')
        
    else :
        pergunta = False
        print('Você acertou a senha!')