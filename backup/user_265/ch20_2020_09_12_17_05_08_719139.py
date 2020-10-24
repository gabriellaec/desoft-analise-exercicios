a = float (input('Distância em km'))
def preço(a):
    if a <= 200:
        def um(b):
            p= 0.5*b
            return p
    resultado= um(a)
    print (resultado:.2f)
    else:
        def dois(c):
            j= 200*0.5 + (c-200)*0.45
            return j
    result= dois(a)
    print(result:.2f)