class Circulo:
    def __init__(self,pc,raio):
        self.centro=pc
        self.traio=float(raio)
    def contem(self,ponto):
        self.ponto=ponto
        self.centro_x=self.centro.x
        self.centro_y=self.centro.y
        self.ponto_x=self.ponto.x
        self.ponto_y=self.ponto.y
        if (((self.ponto_x-self.centro_x)**2)+((self.ponto_y-self.centro_y)**2))<=(self.traio)**2:
            return True
        else:
            return False
        