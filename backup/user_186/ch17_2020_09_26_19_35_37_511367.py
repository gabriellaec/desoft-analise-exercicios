def eh_bissexto (x):
    ano= int(x-2020) 
    return ano

if eh_bissexto % 4:
    print ("True") 
else :
    print ("False") 