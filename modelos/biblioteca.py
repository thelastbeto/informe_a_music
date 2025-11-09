from modelos.midias.midia import Midia

class Biblioteca():
    
    bibliotecas = []
    
    def __init__(self, nome, owner):
        self._nome = nome.title()
        self._disponivel = False
        self._owner = owner
        self._midias = []
        Biblioteca.bibliotecas.append(self)
    
    # Criando metodo especial para exibir no formato de string;  
    def __str__(self):
       return f'A biblioteca {self._nome} está {self._disponivel}. '
       
    # Property - Modifica como um atributo vai ser lido     
    @property
    def disponivel(self):
      return 'Disponível' if self._disponivel == True else 'Indisponível'
  
     # Métodos da classe: não ligados a nenhuma instância, apenas a classe.
     
    @classmethod
    def lista_bibliotecas(cls):
        for i, bibilioteca in enumerate(cls.bibliotecas, start=1):
            mensagem_bibliotecas = f'{i}.Nome: {bibilioteca._nome}\n Criador: {bibilioteca._owner}\n Disponível: {bibilioteca.disponivel}\n'
            print(mensagem_bibliotecas)
        
    @property
    def exibe_midias(self):
        print(f'Exibindo as mídias da biblioteca {self._nome}\n')
        for i, item in enumerate(self._midias, start=1):
            if hasattr(item,'_autor'):
                mensagem_audiobook = f'{i}.Nome: {item._titulo} \n  Conteúdo: {item._conteudo} \n  Tipo: {item._tipo} \n  Autor: {item._autor}\n'
                print(mensagem_audiobook)
            elif hasattr(item,'_apresentador'):
                mensagem_podcast = f'{i}.Nome: {item._titulo} \n  Conteúdo: {item._conteudo} \n  Tipo: {item._tipo} \n  Apresentador: {item._apresentador}\n'
                print(mensagem_podcast)
            elif hasattr(item,'_genero'):
                mensagem_musica = f'{i}.Nome: {item._titulo} \n  Gênero: {item._genero} \n  Tipo: {item._tipo}\n  Artista: {item._artista}\n'
                print(mensagem_musica)
            else:
                mensagem_generica = f'{i}.Nome: {item._titulo} \n  Conteúdo: {item._conteudo} \n  Tipo: {item._tipo} \n'
                print(mensagem_generica)
            
          
    def disponibilizar_bibliotecas(self):
        self._ativo = not self._ativo
    
    def adiciona_midia(self, midia):
        # isisntance, verifica se o objeto é isntancia da classe: isinstance(obj, classe)
        if isinstance(midia, Midia):
            self._midias.append(midia)
        else:
            print('Apenas instância de Mídia!')