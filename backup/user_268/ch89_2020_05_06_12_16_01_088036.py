class Circulo:
    def __init__(self):
        x = self.x
        y = self.y
        centro = (x, y)
       
    def __init__(self, r):
        raio = float(self.r)
       
    def contem(a, b):
        pontox = a
        pontoy = b
        if (pontox - x)**2 + (pontoy - y)**2 <= raio**2:
            return ('o ponto está dentro do círculo')
        else:
            return('o ponto está fora do círculo')