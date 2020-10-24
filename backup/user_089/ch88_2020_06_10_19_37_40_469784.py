class Retangulo:
    def __init__(self,ponto_ie,ponto_sd):
        self.ponto_ie = ponto_ie
        self.ponto_sd = ponto_sd
        
    def calcula_perimetro(self,perimetro):
        self.perimetro = 2*(ponto_ie.x - ponto_sd.x)+2*(ponto_ie.y-ponto_sd.y)
        
    def calcula_area(self):
        self.area = (ponto_sd.x-ponto_ie.x)*(ponto_sd.y-ponto_ie.y)