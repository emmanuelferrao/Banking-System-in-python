class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaCorrente:
    def __init__(self, numero_conta, agencia, saldo, titular):
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = saldo
        self.titular = titular
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R${valor:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: R${valor:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def visualizar_historico(self):
        for transacao in self.historico:
            print(transacao)

def criar_usuario(nome, cpf):
    novo_usuario = Usuario(nome, cpf)
    return novo_usuario

def criar_conta_corrente(numero_conta, agencia, saldo, titular):
    nova_conta = ContaCorrente(numero_conta, agencia, saldo, titular)
    return nova_conta

# Exemplo de uso:
usuario1 = criar_usuario("João da Silva", "12345678901")
conta1 = criar_conta_corrente("0001", "123", 1000, usuario1)

conta1.depositar(500)
conta1.sacar(200)
conta1.visualizar_historico()