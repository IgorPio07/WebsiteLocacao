from website.propriedades import Apartamento
from website.usuario import Corretor

nome_corretor = input('Informe seu nome para começar: ')


def main():
    corretor_1 = Corretor(nome_corretor)
    corretor_1.anunciar()
    corretor_1.anunciar()
    corretor_1.display_portifolio()


if __name__ == '__main__':
    main()

