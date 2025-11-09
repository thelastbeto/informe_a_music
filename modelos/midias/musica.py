from modelos.midias.midia import Midia

class Musica(Midia):
    def __init__(self, titulo, duracao, tipo, conteudo, artista, genero):
        super().__init__(titulo, duracao, tipo, conteudo)
        self._artista = artista
        self._genero = genero
        
    def __str__(self):
        return f'A música {self._titulo} tem como gênero musical o {self._genero} e pertence ao artista {self._artista}'
    
    
    def preco_venda(self):
       pass
   
    def desconto_venda(self):
       pass
   
    def exibe_preco(self):
       pass