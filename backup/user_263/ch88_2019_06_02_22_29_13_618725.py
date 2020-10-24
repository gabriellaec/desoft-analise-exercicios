class Retangulo:
    
    def __init__(self, ponto_INFesquerdo, ponto_SUPdireito):
        ponto1 = ponto_INFesquerdo
        ponto2 = ponto_SUPdireito
        self.ladox = abs(ponto1.x - ponto2.x)
        self.ladoy = abs(ponto1.y - ponto2.y)
        
    def calcula_perimetro(self):
        self.perimetro = 2*self.ladox + 2*self.ladoy
        
    def calcula_area(self):
        self.area = self.ladox * self.ladoy
        