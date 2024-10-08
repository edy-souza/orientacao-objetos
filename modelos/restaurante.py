from modelos.avaliacao import Avaliacao

# Criando as classe do restaurante
class Restaurante: # por padrão o nome da classe inicia com letra Maiúscula
    restaurantes = []
    
    def __init__ (self, nome, categoria):
        self._nome = nome.title()  # Transforma a primeira letra em Maiúscula.
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) #adiciona restaurante na lista restauranteS
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')      

    @property
    def ativo(self):
        return '✅' if self._ativo else '☐'      
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
    def recber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota) 
        self._avaliacao.append(avaliacao)
        
       
