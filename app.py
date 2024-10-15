from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça' , 'Goumert')
restaurante_praca.recber_avaliacao('Gustavo', 10)
restaurante_praca.recber_avaliacao('Bernardo', 8)
restaurante_praca.recber_avaliacao('Luiza', 5)
restaurante_praca.recber_avaliacao('Lukas', 3)
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()