#Pergunta quantos cigarros
Quantos_cigarros = int (input("quantos cigarros?"))
#Pergunta há quantos anos
Quantos_anos = int (input("quantos anos?"))
def t(Quantos_cigarros, Quantos_anos):
    t = Quantos_anos*12*30*Quantos_cigarros*10/1440
    return t
print(t(Quantos_cigarros, Quantos_anos)