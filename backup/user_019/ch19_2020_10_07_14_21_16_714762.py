def classifica_Triangulo (L1,L2,L3):
    if L1 == L2 == L3:
        return ("equilátero")
    elif L1 != L2 != L3: 
        return ("escaleno")
    else L1 == L2 or L3 == L1 or L2 == L3:
        return ("isósceles")
   