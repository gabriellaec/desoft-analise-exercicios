qtde_cigarros = float(input('Quantos cigarros você fuma por dia?'));
qtde_anos = float(input('Há quantos anos você fuma?'));
 
a = qtde_cigarros;
b = qtde_anos;
 
def tempo_perdido(a, b):
    y = (a*365*b/144.0);
    return y;
   
c = tempo_perdido(a, b);
print(c);