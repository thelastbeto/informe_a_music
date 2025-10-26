
class Avaliacao:
    
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self.nota = nota
        
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self,valor):
        
        if not isinstance(valor, (int,float)):
            raise TypeError("A nota deve ser um número.")
        elif valor > 5 or valor < 0 :
            raise ValueError("Sua nota deve estar entre 0 e 5.")
        else:
            self._nota = valor
        
        
        
        
        
        
    
                