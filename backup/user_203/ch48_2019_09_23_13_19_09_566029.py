num=input('Digite um mes do ano: ')
x=['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']  
i=0
while i < 12: 
    if num==x[i]: 
        print(i+1) 
    i+=1 

