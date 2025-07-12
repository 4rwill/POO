from cd import CD
from catalogo import Catalogo

def main():

    cd1 = CD("Music",20,"Random",True,"Daora")
    cd2 = CD("Swag",32,"Jason",False,"Bom Álbum")
    cd3 = CD("Album",15,"Fred",False,"Musica Ruim")



    

    catalogo1 = Catalogo()

    print("##Verificando se tem CD##")
    print("")
    print(catalogo1.tem_cds())

    print("##Inserindo CDS##")
    print("")

    catalogo1.inserir_cd(cd1)
    catalogo1.inserir_cd(cd2)
    catalogo1.inserir_cd(cd3)

    print("##Listando CDS##")
    print("")

    catalogo1.listar_cds()
    print("##Verificando o CD pelo titulos##")
    print("")

    catalogo1.verificar_cd("Music")
    print(catalogo1.verificar_cd("Aleatorio"))

    print("##Verificando se possuo o CD##")
    print("")
    print(catalogo1.verificar_possuo_cd("Music"))
    print(catalogo1.verificar_possuo_cd("Random"))

    print("##Listando os CD que possuo##")
    print("")

    catalogo1.listar_cds_que_possuo()
    





if __name__ == "__main__":
    main()