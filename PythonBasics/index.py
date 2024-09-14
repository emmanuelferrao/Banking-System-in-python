class ContaBancaria:
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0   

        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")   

        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque:   
 R${valor:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def visualizar_extrato(self):
        print(f"\nExtrato da conta de {self.titular}")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}\n")


conta1 = ContaBancaria("João da Silva", 12345)


conta1.depositar(1000)
conta1.sacar(200)
conta1.depositar(500)
conta1.visualizar_extrato()