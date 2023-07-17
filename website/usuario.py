from website.propriedades import Apartamento


class Corretor:

    def __init__(self, nome):
        self.__nome = nome
        self.portifolio = []

    def display_portifolio(self):
        print(f'Portifolio do Corretor: {self.__nome}')
        for apartamento in self.portifolio:
            apartamento.display()

    def anunciar(self):
        init_args = Apartamento.prompt_init()
        self.portifolio.append(Apartamento(**init_args))
