class Retangulo:
    
    def __init__(self, ponto_inferior_esquerdo, ponto_superior_direito):
        self.tamanho_x = ponto_superior_direito.x - ponto_inferior_esquerdo.x
        self.tamanho_y = ponto_inferior_esquerdo.y - ponto_superior_direito.y
        
        if ponto_inferior_esquerdo.x > ponto_superior_direito.x:
            self.tamanho_x = ponto_inferior_esquerdo.x - ponto_superior_direito.x
        if ponto_superior_direito.y > ponto_inferior_esquerdo.y:
            self.tamanho_y = ponto_superior_direito.y - ponto_inferior_esquerdo.y
    
    def calcula_perimetro(self):
        return self.tamanho_x*2 + self.tamanho_y*2
    
    def calcula_area(self):
        return self.tamanho_x*self.tamanho_y