class Filme:
    '''Um filme'''
    
    def __init__(self):
        self.__titulo = ''
        self.__ano = 0
        self.__nota = 0.0
        
    @property
    def titulo(self):
        return self.__titulo
        
    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nova_nota):
        self.__nota = nova_nota

    def __repr__(self):
        return f'{self.__titulo} ({self.__ano}) - {self.__nota}'

    
class FilmotecaModel:
    '''Modelo: opera filmoteca'''
    
    def __init__(self):
        self._listaFilmes = []
    
    def inserir(self, novo_filme):
        self._listaFilmes.append(novo_filme)
    
    def atualizar(self, indice, novo_filme):
        self._listaFilmes[indice] = novo_filme
    
    def remover(self, valor):
        if type(valor) == Filme:
            self._listaFilmes.remove(valor)
        elif type(valor) == int:
            self._listaFilmes.pop(valor)
        
    def __repr__(self):
        return str(self._listaFilmes)

# Código de teste para o Model
if __name__ == '__main__':
    f1 = Filme()
    f1.titulo = 'AAAAA'
    f1.ano = 2020
    f1.nota = 7.0

    f2 = Filme()
    f2.titulo = 'BBBBB'
    f2.ano = 1980
    f2.nota = 5.0
    
    meus_filmes = FilmotecaModel()
    meus_filmes.inserir(f1)
    meus_filmes.inserir(f2)
    meus_filmes.inserir(f1)
    meus_filmes.inserir(f1)
    meus_filmes.inserir(f1)
    
    print(meus_filmes)
    
    f3 = Filme()
    f3.titulo = 'xaxaxaxaax'
    f3.ano = 2000
    f3.nota = 9.4
    print(f3)
    
    meus_filmes.atualizar(3, f3)
    print(meus_filmes)
    
    meus_filmes.remover(f1)
    print(meus_filmes)
    meus_filmes.remover(3)
    print(meus_filmes)