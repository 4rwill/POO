class Conta:
    def __init__(self,nome: str, numero: int):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = 0.0
        self.__flag = True


    def getNome(self):
        return self.__nome
        
    def getNumero(self):
        return self.__numero
        
    def getSaldo(self):
        return self.__saldo
        
    def getFlag(self):
        return self.__flag



    def setNome(self, nome: str):
        if not isinstance(nome, str) or len(nome) == 0:
            raise ValueError("O nome do correntista não pode ser vazio.")
        self.__nome = nome
   
    def setNumero(self, numero: int):
        if not isinstance(numero, int) or numero <= 0:
            raise ValueError("O Número da conta deve ser maior que 0")
        self.__numero = numero
   
    def setSaldo(self, saldo: float):
        self.__saldo = saldo

    def setFlag(self, flag: bool):
        if not isinstance(flag, bool):
            raise TypeError("A flag da conta deve ser um valor booleano.")
        self.__flag = flag        
        

    def depositar(self,valor: float):
        if not self.__flag:
            raise Exception("Operação não permitida: Conta inativa.") 
        if valor <= 0:
                raise ValueError("O valor do depósito deve ser positivo.")
        
        self.__saldo += valor
           
            

    def sacar(self, valor: float):
        if not self.__flag:
            raise Exception("Operação não permitida: Conta inativa.")
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if self.__saldo < valor:
            raise ValueError("Saldo insuficiente para o saque.")
        self.__saldo -= valor

    def imprime(self):
            print("-" * 30)
            print(f"Correntista: {self.getNome()}")
            print(f"Número da Conta: {self.getNumero()}")
            print(f"Saldo Disponível: R$ {self.getSaldo():.2f}")
            status = "Ativa" if self.getFlag() else "Inativa"
            print(f"Status da Conta: {status}")
            print("-" * 30)            