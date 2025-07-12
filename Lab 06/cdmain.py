from cd import CD
from catalogo import Catalogo

def main():
   
    cd1 = CD("Music",20,"Random",False,"Daora")
    cd2 = CD("Swag",32,"Jason",False,"Bom Álbum")
    cd3 = CD("Album",15,"Fred",True,"Musica Ruim")

    cd1.imprime()
    cd1.set_artista("Mudado")
    cd1.set_comentario("Comentário novo")
    cd1.imprime()

if __name__ == "__main__":
    main() 