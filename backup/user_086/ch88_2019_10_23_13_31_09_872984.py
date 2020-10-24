class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.psd=ponto2
        self.pie=ponto1
    def calcula_perimetro(self):
        per=abs(2*(self.psd.x-self.pie.x))+abs(2*(self.pie.y-self.psd.y))
        return per
    def calcula_area(self):
        area=abs(self.psd.x-self.pie.x)*abs(self.pie.y-self.psd.y)
        return area