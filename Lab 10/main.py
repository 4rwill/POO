from conta import Conta

def main():
    sucesso = True
    while sucesso:
        try:
            minha_conta = Conta("Will", 1020)
            #minha_conta.setFlag(False)

            minha_conta.imprime()

            print("\nDepositando R$ 500.00...")
            minha_conta.depositar(500)
            minha_conta.imprime()

            print("\nSacando R$ 150.00...")
            minha_conta.sacar(150)
            minha_conta.imprime()

            sucesso = False

        except Exception as e:
            print(f"Erro: {e}. \nTENTE NOVAMENTE!")
            sucesso = False



if __name__ == "__main__":
    main()    