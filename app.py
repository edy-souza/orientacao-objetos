from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça' , 'Goumert')
restaurante_praca.recber_avaliacao('Gustavo', 10)
restaurante_praca.recber_avaliacao('Bernardo', 8)
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()