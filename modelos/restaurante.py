# Criando as classe do restaurante
class Restaurante: # por padrão o nome da classe de iniciar com letra Maiúscula
    restaurantes = []
    
    def __init__ (self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) #adiciona restaurante na lista restauranteS
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')            
       
# instanciando uma classe com seu objeto    
restaurante_praca = Restaurante('Praça' , 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express' , 'Italiano')

Restaurante.listar_restaurantes()