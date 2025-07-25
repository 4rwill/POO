from veiculo import Veiculo
from carro import Carro
from moto import Moto
from bicicleta import Bicicleta

def main():

    carro1 = Carro("Lancer", "Mitsu", 4,2, "Bom")
    carro1.imprime()
    carro1.emite_som()

    moto1 = Moto("Pop100", "Honda", 2,100, "A melhor que tem")
    moto1.imprime()
    moto1.emite_som()

    bicicleta1 = Bicicleta("Aro 26", "Monark", 2,6, "Já vi melhores")
    bicicleta1.imprime()
    bicicleta1.emite_som()







if __name__ == "__main__":
    main()