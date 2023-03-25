#SerVivo--> atributos pontos_vida / pontos_ataque. 
 #classe Personagem tem q ser sub de SerVivo com atributo nome. 
  #classe Monstro sub de SerVivo com um atributo tipo.
   #+ classes Lobo e Golble sub de Monstro, atribuir a Lobo força e Goblin inteligencia.
    # Colocar super() chamar-->pai .


class SerVivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = 0
        self.pontos_ataque = 0

class Personagem(SerVivo):
    def __init__(self, nome, pontos_vida, pontos_ataque):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

class Monstro(SerVivo):
    def __init__(self, tipo, pontos_vida, pontos_ataque):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo

class Bobo(Monstro):
    def __init__(self, tipo, pontos_vida, pontos_ataque, forca):
        super().__init__(tipo, pontos_vida, pontos_ataque)
        self.forca = forca

class Goblin(Monstro):
    def __init__(self, tipo, pontos_vida, pontos_ataque, inteligencia):
        super().__init__(tipo, pontos_vida, pontos_ataque)
        self.inteligencia = inteligencia