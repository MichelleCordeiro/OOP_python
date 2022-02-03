class ExcecaoBase(Exception):
    pass

class ExcecaoTituloLivro(ExcecaoBase):
    pass

class ExcecaoAnoLivro(ExcecaoBase):
    pass

class ExcecaoCodLivro(ExcecaoBase):
    pass

class ExcecaoLivro(ExcecaoBase):
    pass

class ExcecaoCodDuplicado(ExcecaoBase):
    pass

class ExcecaoLivroDuplicado(ExcecaoBase):
    pass


class Livro():
    def __init__(self):
        self.__titulo = ''
        self.__ano = 0
        self.__cod = ''
        
    @property
    def titulo(self):
        return self.__titulo
        
    @titulo.setter
    def titulo(self, novo_titulo):
        if novo_titulo != '':
            self.__titulo = novo_titulo
        else:
            raise ExcecaoTituloLivro('Título do livro deve ser uma string não vazia')
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, novo_ano):
        if 1400 <= novo_ano <= 2100:
            self.__ano = novo_ano
        else:
            raise ExcecaoAnoLivro('O ano deve estar entre 1400 e 2100')

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, novo_cod):
        if len(str(novo_cod)) >= 6 :
            self.__cod = str(novo_cod)
        else:
            raise ExcecaoCodLivro('O ISBN deve conter pelo menos 6 caracteres.')    
    
    def __repr__(self):
        return f'Livro: [{self.__titulo}, {self.__ano}, {self.__cod}]'


class Biblioteca(Livro):
    def __init__(self):
        Livro.__init__(self)
        self.__bib = []
        
    def cadastra(self, novo_livro):
        if type(novo_livro) == Livro:
            for i in range(len(self.__bib)):                
                if (novo_livro.cod == self.__bib[i].cod) and (novo_livro.ano != self.__bib[i].ano):
                    raise ExcecaoCodDuplicado('Livros diferentes não podem ter o mesmo código ISBN.')
                elif (novo_livro.cod == self.__bib[i].cod) and (novo_livro.ano == self.__bib[i].ano) and (novo_livro.titulo == self.__bib[i].titulo):
                    raise ExcecaoLivroDuplicado('A biblioteca não pode armazenar um mesmo livro mais de uma vez.')
            self.__bib.append(novo_livro)
        else:
            raise ExcecaoLivro('Objeto precisa ser do tipo Livro')

    def __repr__(self):
        return f'Biblioteca: {str(self.__bib)}'
                
        
if __name__ == "__main__":
    l1 = Livro()
    l1.titulo = 'aaaaaaa'
    l1.ano = 2020
    l1.cod = 5555555
    print(l1)
    l2 = Livro()
    l2.titulo = 'bbbbbbb'
    l2.ano = 2010
    l2.cod = 654321
    print(l2)
    
    library = Biblioteca()
    library.cadastra(l1)
    library.cadastra(l2)
    print(library)
    
    try:
        liv = Livro()
        liv.titulo = ''
    except ExcecaoTituloLivro as err:
        print(f'\n{type(err).__name__}: {err}')
        liv.titulo = input('Insira um novo título para o livro: ')

    try:     
        liv.ano = 1100
    except ExcecaoAnoLivro as err:
        print(f'\n{type(err).__name__}: {err}')
        liv.ano = int(input('Insira um novo ano válido para o livro: '))
        
    try:
        liv.cod = '1a3a5'
    except ExcecaoCodLivro as err:
        print(f'\n{type(err).__name__}: {err}')
        liv.cod = input('Insira um novo código válido para o livro: ')
        print('\n', liv)

    try:
        liv2 = 'string'
        library.cadastra(liv2)
    except ExcecaoLivro as err:
        print(f'\n{type(err).__name__}: {err}')
        
    try:
        liv3 = Livro()
        liv3.titulo = l1.titulo
        liv3.ano = l1.ano+50  #Edições diferentes -> livros diferentes
        liv3.cod = l1.cod
        library.cadastra(liv3)
    except ExcecaoCodDuplicado as err:
        print(f'\n{type(err).__name__}: {err}')

    try:
        liv4 = Livro()
        liv4.titulo = l2.titulo
        liv4.ano = l2.ano
        liv4.cod = l2.cod
        library.cadastra(liv4)
    except ExcecaoLivroDuplicado as err:
        print(f'\n{type(err).__name__}: {err}')
        
    print('\n', library)