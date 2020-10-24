class Circulo:
    
    def __init__(self, VPonto, VRaio):
        self.ponto = VPonto
        self.raio = float(VRaio)
        
    def PertenceAoCirculo (self, OutroPontoTeste):
        distancia = self.center.distance_to(OutroPontoTeste)
        return distancia <= self.raio