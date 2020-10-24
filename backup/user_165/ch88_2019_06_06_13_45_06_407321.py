class Retangulo():
    def __init__(self,Ponto1,Ponto2):
        self.Ponto1_x = Ponto1.x
        self.Ponto1_y= Ponto1.y
        self.Ponto2_x = Ponto2.x
        self.Ponto2_y= Ponto2.y
    def calcula_perimetro(self):
        lado_x = (self.Ponto1_x - self.Ponto2_x)**2
        lado_y = (self.Ponto1_y-self.Ponto2_y)**2
        p = lado_x+lado_y
        return p
    def calcula_area(self):
        area = (self.Ponto1_x - self.Ponto2_x)*(self.Ponto1_y-self.Ponto2_y)
        return area 
        