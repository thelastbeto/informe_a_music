from modelos.avaliacao import Avaliacao


class Musica:
    
    musicas_favoritas = []
    
    def __init__(self, nome, artista, duracao=int):
        self._nome = nome.title()
        self._artista = artista.title()
        self._duracao = duracao
        self._disponivel = False
        self._avaliacao = []
        Musica.musicas_favoritas.append(self)
      
    # Criando metodo especial para exibir no formato de string;  
    def __str__(self):
       return f'{self._nome}-{self.artista} -{self.duracao} - {self.disponivel}'
    
     
    @property
    def disponivel(self):
      return 'Disponível' if self._disponivel == True else 'Indisponível'
   
    # Métodos da classe: não ligados a nenhuma instância, apenas a classe.
    @classmethod
    def lista_musicas(cls):
        print(f'{"Nome da música".ljust(25)} | {"Nome do artista".ljust(25)} | {"Duração".ljust(25)} | {"Avaliação".ljust(25)} | {"Disponibilidade na plataforma"}\n')
        for x in cls.musicas_favoritas:
          print(f'{x._nome.ljust(25)} | {x._artista.ljust(25)} | {str(x._duracao).ljust(25)} | {str(x.calcula_media).ljust(25)} | {x.disponivel}')
          
    def disponibilizar_musicas(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property    
    def calcula_media(self):
        if not self._avaliacao:
            return f'Não possui avaliações.'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_das_notas/qtd_notas, 1)
        return media
    
    def lista_avaliacao(self):
        recebe_media = self.calcula_media()
        print(f'A média das notas da música {self._nome} é {recebe_media}')
        
    
        

        
        
    # Property - Modifica como um atributo vai ser lido


# Verificando com VARS:
# print(musica_1)

