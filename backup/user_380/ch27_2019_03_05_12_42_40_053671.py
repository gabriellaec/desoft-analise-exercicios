qtde_cigarros = int(input('Quantos cigarros você fuma por dia?'));
qtde_anos = int(input('Há quantos anos você fuma?'));
 
a = qtde_cigarros;
b = qtde_anos;
 
def tempo_perdido(a, b):
    y = (a/144)*365*b;
    return y;
   
c = tempo_perdido(a, b);
print(c);