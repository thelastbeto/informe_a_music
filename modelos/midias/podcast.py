from modelos.midias.midia import Midia

class PodCast(Midia):
    def __init__(self, titulo, duracao, conteudo,tipo, apresentador):
        super().__init__(titulo, duracao, tipo, conteudo)
        self._apresentador = apresentador
        
    def __str__(self):
        return super().__str__()
    
    def preco_venda(self):
        return 50.0
        
    def desconto_venda(self):
        # Calcula o preco real com o desconto da black friday;
        preco = self.preco_venda()
        preco -= preco * 0.15
        return preco
    
    def exibe_preco(self):
        novo_preco = self.desconto_venda()
        print(f' O custo do {self._tipo} é R${novo_preco}!')
        