class Apartamento:

    def __init__(self, titulo, endereco, preco, condominio, iptu, metros, quartos, banheiros, vagas):
        self.__titulo = titulo
        self.__endereco = endereco
        self.__preco = preco
        self.__condominio = condominio
        self.__iptu = iptu
        self.__metros = metros
        self.__quartos = quartos
        self.__banheiros = banheiros
        self.__vagas = vagas

    def display(self):
        print()
        print('Detalhes da venda')
        print('==================')
        print(f'{self.__titulo}')
        print(f'Endereço: {self.__endereco}')
        print(f'Preço: {self.__preco}')
        print(f'Condominio: {self.__condominio}')
        print(f'IPTU: {self.__iptu}')
        print(f'Metros Quadrados: {self.__metros}')
        print(f'Quartos: {self.__quartos}')
        print(f'Banheiros: {self.__banheiros}')
        print(f'Vgas: {self.__vagas}')
        print('====================')

    @staticmethod
    def prompt_init():
        return dict(titulo=input('Informe o Título do Anúncio'),
                    endereco=input('Informe o endereço'),
                    preco=input('Informe o preço'),
                    condominio=input('Informe o valor do condominio'),
                    iptu=input('Informe o valor do IPTU'),
                    metros=input('Informe quantos metros quadrados tem o apartamento'),
                    quartos=input('Informe quantos quartos tem o local'),
                    banheiros=input('Informe quantos banheiros tem, o local'),
                    vagas=input('Informe a quantidade de vagas'))
