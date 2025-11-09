from modelos.midias.midia import Midia

class Audiobook(Midia):
    def __init__(self, titulo, duracao, conteudo, tipo, autor):
        super().__init__(titulo, duracao, tipo, conteudo)
        self._autor = autor
        
    def __str__(self):
        return super().__str__()
    
    # Os métodos abstratos estão sendo aplicados, porém, caso eu não queira utilizar nenhuma regra para tal, poderemos usar o "pass";
    
    def preco_venda(self):
        return 25.0
        
    def desconto_venda(self):
        # Calcula o preco real com o desconto da black friday;
        preco = self.preco_venda()
        preco -= preco * 0.10
        return preco
    
    def exibe_preco(self):
        novo_preco = self.desconto_venda()
        print(f' O custo do {self._tipo} é R${novo_preco}!')
    
    