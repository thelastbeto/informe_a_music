from modelos.avaliacao import Avaliacao
from abc import ABC, abstractmethod

class Midia(ABC):
    
    def __init__(self, titulo, duracao, tipo, conteudo):
        self._titulo = titulo
        self._duracao = duracao
        self._tipo = tipo
        self._conteudo = conteudo
        self._disponivel = False
        self._avaliacao = []

        
    def __str__(self):
        return f'O {self._tipo} {self._titulo} tem como conteúdo principal tratar sobre {self._conteudo}.'
    
    def __str__(self):
       return f'A biblioteca {self._nome} está {self._disponivel}. '
   
    @abstractmethod
    def preco_venda(self):
       pass
   
    @abstractmethod
    def desconto_venda(self):
       pass
   
    @abstractmethod
    def exibe_preco(self):
       pass

    @property
    def disponivel(self):
      return 'Disponível' if self._disponivel == True else 'Indisponível'
   
    def calcula_media(self):
        if not self._avaliacao:
            return f'Não possui avaliações.'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd_notas = len(self._avaliacao)
        media = round(soma_das_notas/qtd_notas, 1)
        return media
            
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    def lista_avaliacao(self):
        recebe_media = self.calcula_media()
        print(f'A média das notas da biblioteca {self._titulo} é {recebe_media}')
        