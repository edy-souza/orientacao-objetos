# Criando as classe do restaurante
class Restaurante: # por padrão o nome da classe de iniciar com letra Maiúscula
    restaurantes = []
    
    def __init__ (self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self) #adiciona restaurante na lista restauranteS
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')      
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'      
       
# instanciando uma classe com seu objeto    
restaurante_praca = Restaurante('Praça' , 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express' , 'Italiano')

Restaurante.listar_restaurantes()