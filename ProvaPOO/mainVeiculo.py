from veiculo import Veiculo
from carro import Carro
from caminhao import Caminhao

def main():
    carro1 = Carro("Fabricante", "Placa", 0)
    caminhao1 = Caminhao("Fabricante", "Placa")

    try:
        #Teste 1 (Testando métodos)

        #CARRO
        carro1.setFabricante("Mitsubishi")
        carro1.setPlaca("NSF7712")
        carro1.setConsumo(20)
        carro1.setPortas(4)
        carro1.setNivelCombustivel(40)

        print("Carro antes do TESTE 1\n")
        carro1.imprime()
        print("")

        carro1.abastecer(10)
        print(f"Nível de Gasolina Após abastecer: {carro1.gasolina()}")
        carro1.mover(20)
        print(f"Nível de Gasolina Após mover: {carro1.gasolina()}\n")

        print("Carro pós TESTE 1 \n")
        carro1.imprime()
        print("-"*40)


        #CAMINHÃO
        caminhao1.setFabricante("Scania")
        caminhao1.setPlaca("JDK1212")
        caminhao1.setNumeroRodas(8)
        caminhao1.setCapacidadeCarga(9)

        print("Caminhão antes do TESTE 1\n")
        caminhao1.imprime()
        print("")

        caminhao1.setCapacidadeCarga(10)
        
        print("Caminhão pós TESTE 1 \n")
        caminhao1.imprime()
        print("-"*40)



        #Teste 2 (Except do mover() e setCapacidadeCarga() )
        
        sucessoMover = False
        while not sucessoMover:
            kmParaMover = int(input("Quantos Km deseja realizar?"))
            
            try:
                carro1.mover(kmParaMover) #Testando fazer um percuso que a gasolina não é capaz de atender  
                sucessoMover = True
                print(f"Gasolina após mover: {carro1.gasolina()}")
            except Exception as e:
                print(f"{e.__class__.__name__}: {e}\n")



        sucessoSetCapacidadeCarga = False
        while not sucessoSetCapacidadeCarga:
            cargaParaSetar = int(input("Quanto de carga voce deseja ter no caminhão?"))

            try:
                caminhao1.setCapacidadeCarga(cargaParaSetar)
                sucessoSetCapacidadeCarga = True
                print(f"Capacidade de carga atual: {caminhao1.getCapacidadeCarga()}")
            except Exception as e:
                print(f"{e.__class__.__name__}: {e}\n")

        




        


    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        


    







if __name__ == "__main__":
    main()    
