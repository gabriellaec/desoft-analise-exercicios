qtde_cigarros = int(input('Quantos cigarros você fuma por dia?'));
qtde_anos = float(input('Há quantos anos você fuma?'));
 
a = qtde_cigarros;
b = qtde_anos;
 
def tempo_perdido(a, b):
    y = b*10/(60*24)*a*365;
    return y;
   
c = tempo_perdido(a, b);
print(c);