
from catalogo import Catalogo
from cd import CD
from dvd import DVD

def main():
   
    meu_catalogo = Catalogo()


    # Criação e inserção de itens (CDs e DVDs) fora de ordem [cite: 40, 41]
    dvd1 = DVD("Matrix", 136, "Wachowski", True, "Clássico da ficção científica.")
    cd1 = CD("Abbey Road", 47, "The Beatles",True, "Último álbum gravado pela banda.")
    dvd2 = DVD("Interestelar", 169, "Christopher Nolan", False, "Ótima ficção científica.")
    
    
    #LISTANDO ANTES DE INSERIR
    meu_catalogo.listar_itens()
    
    
    meu_catalogo.inserir_item(dvd1)
    meu_catalogo.inserir_item(cd1)
    meu_catalogo.inserir_item(dvd2)

    meu_catalogo.listar_itens()

    meu_catalogo.pesquisar_item("Titanic")


    

if __name__ == "__main__":
    main()