from modelos.musica import Musica
from modelos.utilidades import limpa




musica_1 = Musica('Everyday', 'Logic', 204)
musica_2 = Musica('Gold Teeth Gizzle', 'B.G', 237)
musica_3 = Musica('Mind of a Stoner', 'Machine Gun Kelly', 247)
musica_4 = Musica('Starlight', 'Muse', 240)
musica_1.receber_avaliacao('Roberto',5)
musica_1.receber_avaliacao('Duda',4.5)
musica_1.receber_avaliacao('Marcela',5)
musica_2.receber_avaliacao('Roberto',5)
musica_3.receber_avaliacao('Roberto',5)
musica_3.receber_avaliacao('Duda',4)




def main():
    Musica.lista_musicas()
    limpa()



if __name__ == '__main__':
    main()