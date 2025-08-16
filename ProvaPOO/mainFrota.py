from veiculo import Veiculo
from carro import Carro
from caminhao import Caminhao
from frota import Frota

def main():

    frota = Frota()
    carro1 = Carro("Fabricante", "Placa", 0)
    caminhao1 = Caminhao("Fabricante", "Placa")
    caminhao2= Caminhao("MARCA","STD2041")
    teste =1

    #CARRO
    carro1.setFabricante("Mitsubishi")
    carro1.setPlaca("NSF7712")
    carro1.setConsumo(20)
    carro1.setPortas(4)
    carro1.setNivelCombustivel(40)
    
    #CAMINHÃO
    caminhao1.setFabricante("Scania")
    caminhao1.setPlaca("JDK1212")
    caminhao1.setNumeroRodas(8)
    caminhao1.setCapacidadeCarga(9)

    #Adicionando na Frota
    frota.inserirVeiculos(caminhao1)
    frota.inserirVeiculos(carro1)

    #Listando veiculos
    frota.listarVeiculos()
    
    #Removendo veiculo
    frota.removerVeiculos(caminhao1)

    #Listando veiculos apos remover caminhão
    frota.listarVeiculos()    

    #Veficando se ta vazia
    print(f"A frota está vazia: {frota.frotaVazia()}")





if __name__ == "__main__":
    main()