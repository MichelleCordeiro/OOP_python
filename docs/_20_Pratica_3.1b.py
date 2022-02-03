class ExcecaoSistema(Exception):
    pass

class ExcecaoTituloLivro(ExcecaoSistema):
    pass

class ExcecaoAnoLivro(ExcecaoSistema):
    pass

class ExcecaoCodLivro(ExcecaoSistema):
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
            raise ExcecaoTituloLivro('Título do livro deve ser uma string não vazia.\n')
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, novo_ano):
        if int(novo_ano) > 1400 and int(novo_ano) < 2100:
            self.__ano = novo_ano
        else:
            raise ExcecaoAnoLivro('O ano deve estar entre 1400 e 2100.\n')

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, novo_cod):
        if len(str(novo_cod)) >= 6 :
            self.__cod = str(novo_cod)
        else:
            raise ExcecaoCodLivro('O ISBN deve conter pelo menos 6 caracteres.\n')    
    
    def __repr__(self):
        return f'Livro: [{self.__titulo}, {self.__ano}, {self.__cod}]'


class LeitorLivros(Livro):
    def __init__(self, nome_arquivo):
        Livro.__init__(self)
        self.nome_arquivo = nome_arquivo
        self.livros = []
        self.arquivo = ''
    
    def processa(self):
        with open(self.nome_arquivo, 'r') as self.arquivo:
            n = int(self.arquivo.readline())    # qtd. de livros no arquivo
            for i in range(n):
                try:
                    l = Livro()    # Instancia o livro
                    l.titulo = self.arquivo.readline().rstrip()    # Obtém título sem a quebra de linha
                    l.ano = self.arquivo.readline().rstrip()   # Obtém ano sem a quebra de linha
                    l.cod = self.arquivo.readline().rstrip()    # Obtém ISBN sem a quebra de linha
                except ExcecaoSistema as err:
                    print(f'\n{type(err).__name__}: {err} - Erro no livro {i+1}\n')
                    if type(err).__name__ == 'ExcecaoTituloLivro':
                        self.arquivo.readline()    # Reposiciona o ponteiro p a linha seguinte
                        self.arquivo.readline()    # Repoosiciona o ponteiro p o próximo livro/título
                    elif type(err).__name__ == 'ExcecaoAnoLivro':
                        self.arquivo.readline()    # Repoosiciona o ponteiro p o próximo livro/título
                else:
                    self.livros.append([l.titulo, l.ano, l.cod])    # Adiciona livro à self.livros
        
if __name__ == "__main__":
    nom_arq = input('Insira o nome do arquivo: ')
    leitor = LeitorLivros(nom_arq)
    leitor.processa()

    print('Livros lidos corretamente do arquivo:')
    for l in leitor.livros:
        print('\t' + str(l))