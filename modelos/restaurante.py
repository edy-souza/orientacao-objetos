# Criando as classe do restaurante
class Restaurante: # por padrão o nome da classe de iniciar com letra Maiúscula
    restaurantes = []
    
    def __init__ (self, nome, categoria):
        self._nome = nome.title()  # Transforma a primeira letra em Maiúscula.
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self) #adiciona restaurante na lista restauranteS
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes():
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')      

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'      
       
# instanciando uma classe com seu objeto    
restaurante_praca = Restaurante('praça' , 'Gourmet')
restaurante_pizza = Restaurante('pizza Express' , 'Italiano')

Restaurante.listar_restaurantes()