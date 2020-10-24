class Retangulo:
    def __init__(self, pie, psd):
        self.pie= pie
        self.psd=psd
    def calcula_perimetro(self):
        h= self.pie.y-self.psd.y
        l= self.pie.x-self.psd.x
        p= h+h+l+l
        return p
    def calcula_area(self):
        h= self.psd.y-self.pie.y
        l= self.pie.x-self.psd.x
        a= h*l
        return a
    