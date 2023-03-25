class contabancaria:
    def _init_(self, titular, saldo):
        self.titular= titular
        self.saldo = saldo

        def depositar(self, valor):
            self.saldo = self.saldo + valor
            
        def sacar(self, valor):
            if (valor <= self.saldo):
                self.saldo = self.saldo - valor
            else:
                print("Seu saldo é isuficiente!")

        def consultar_saldo(self):
                print(f"Saldo atual:R${self.saldo:.2f}")
