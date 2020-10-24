class Circulo:
    def __init__(self, ponto, raio):
        self.pontox = ponto.x
        self.pontoy = ponto.y
        self.raio = raio
        
    def contem(self, ponto):
        if (self.pontox - ponto.x)**2 + (self.pontoy - ponto.y)**2 > self.raio**2:
            resposta = False
        else: 
            resposta = True 
        return resposta