class UnaEletronica:

  def __init__(self):
      self.candidatos = [
                          {"nome_do_candidato": "ana", "partido": "laranja"}, 
                          {"nome_do_candidato": "bia", "partido": "verde"},
                          {"nome_do_candidato": "anne","partido": "azul"}
                        ]

  def exibe_candidatos(self):
        for candidato in self.candidatos: 
            print(candidato.get("nome_do_candidato")) 
            print(candidato.get("partido"))

  def adicionar_novo_candidato(self, nome_do_candidato, partido): 
      self.candidatos.append({"nome_do_candidato": nome_do_candidato, "partido": partido})

  def remove_ultimo_candidato(self):
      #self.candidatos.pop()

     def __init__(self):
      self.teste = []

urna = UnaEletronica()

urna.exibe_candidatos()
print("###############################")

urna.adicionar_novo_candidato ("Joao teste", "roxo")
print("########################")

urna.exibe_candidatos()
print("########################")

urna.remove_ultimo_candidato()
print("########################")

urna.exibe_candidatos()
print("########################")                   
                        #Pasta ps4 exemplos em aula