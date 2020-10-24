def toma_multa(v):
    if v>80:
        resultado= 5*(v-80) 
        return str(resultado) + " de multa"
    
    else:
        return "nao toma multa"
    
velocidade= int(input("qual a velocidade?: "))
final= toma_multa(velocidade)
print(final)