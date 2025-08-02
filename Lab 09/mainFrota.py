from veiculo import Veiculo
from carro import Carro
from moto import Moto
from bicicleta import Bicicleta
from frota import Frota

def main():

    minhaFrota = Frota()

    carro1: Carro = Carro("Lancer", "Mitsu", 4, 2, "Bom")
    moto1: Moto = Moto("Pop100", "Honda", 2, 100, "A melhor que tem")
    bicicleta1: Bicicleta = Bicicleta("Aro 26", "Monark", 2, 6, "Já vi melhores")


    minhaFrota.inserir_veiculo(moto1)
    minhaFrota.inserir_veiculo(carro1)
    minhaFrota.inserir_veiculo(bicicleta1)

    minhaFrota.remover_veiculo(bicicleta1)
    minhaFrota.remover_moto(moto1)

    minhaFrota.frota_vazia()
    minhaFrota.frota_sem_motos()

    minhaFrota.inserir_veiculo(moto1)

    minhaFrota.buscar_carro_por_modelo("Lancer")

    minhaFrota.listar_frota()
    

if __name__ == "__main__":
    main()