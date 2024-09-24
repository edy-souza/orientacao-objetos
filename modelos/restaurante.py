# Criando as classe do restaurante
class Restaurante:
    def __init__ (self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

# instanciando uma classe com seu objeto    
restaurante_praca = Restaurante('Praça' , 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express' , 'Italiano')

restarantes = [restaurante_pizza , restaurante_pizza]
print(restaurante_pizza)
print(restaurante_praca)