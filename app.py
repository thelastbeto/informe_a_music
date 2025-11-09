from modelos.midias.musica import Musica
from modelos.biblioteca import Biblioteca
from modelos.utilidades import limpa
from modelos.midias.audiobook import Audiobook
from modelos.midias.podcast import PodCast

# Criando biblioteca:
biblioteca_1 = Biblioteca('Machine Gun Bobby', 'Roberto Jr')
biblioteca_2 = Biblioteca('Tunts Tunts', 'Eduarda Araújo')

# Teste música:
musica_1 = Musica('Gold Teeth Gizzle', 237, 'Musica', 'Riqueza', 'B.G' ,'Rap')
musica_2 = Musica('Ocean Drive', 206, 'Musica', 'Drive', 'Duke Dumont', 'Dance')
biblioteca_1.adiciona_midia(musica_1)
biblioteca_2.adiciona_midia(musica_2)
musica_1.receber_avaliacao('Roberto',5)
musica_1.receber_avaliacao('Duda',4.5)
musica_1.receber_avaliacao('Marcela',5)
musica_2.receber_avaliacao('Roberto',5)
musica_2.receber_avaliacao('Duda',5)
musica_2.receber_avaliacao('Marcela',5)

# Teste Podcast:
podcast_1 = PodCast('O IronMan 70.3', 120, 'Esportes', 'PodCast', 'Roberto Jr')
biblioteca_1.adiciona_midia(podcast_1)

#Teste audiobook:
audiobook_1 = Audiobook('Esportes de Endurance', 30, 'Esportes', 'AudioBook','Roberto Jr')
biblioteca_1.adiciona_midia(audiobook_1)



def main():
    Biblioteca.lista_bibliotecas()
    biblioteca_2.exibe_midias
    musica_2.lista_avaliacao()
    #@ limpa()



if __name__ == '__main__':
    main()