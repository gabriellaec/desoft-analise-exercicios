#Pergunta quantos cigarros
Quantos_cigarros = float (input("quantos cigarros?"))
#Pergunta há quantos anos
Quantos_anos = float (input("quantos anos?"))
def t(Quantos_cigarros, Quantos_anos):
    t = Quantos_anos*365*Quantos_cigarros*10/1440
    return t
print(t)