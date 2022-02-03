from Pratica32b_FilmotecaModel import FilmotecaModel, Filme
from Pratica32b_FilmotecaView import FilmotecaView
import tkinter as tk


class FilmotecaController:
    '''Controlador opera o Modelo a partir da View e devolve os resultados para a View'''
    
    def __init__(self):
        self.model = None
        self.view = None

        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title('Filmoteca TK')

    def inicializa(self, model, view):
        ''' Método faz parte da interface pública: atribui view e model
        e em seguida, configura o controlador com o view e model.  '''
        self.model = model
        self.view = view
        self._configura()

    def _configura(self):
        '''Método privado: configura ações para a visualização (eventos Tk)'''
        self.view.nota_var.set(0.0)
        
        self.view.botoes['Insere']['command'] = lambda: self._processa_entrada('insere')
        self.view.botoes['Atualiza']['command'] = lambda: self._processa_entrada('atualiza')
        self.view.botoes['Remove']['command'] = lambda: self._processa_entrada('remove')

    def executa(self):
        '''Método principal da interface pública da classe.'''
        tk.mainloop()

    def _processa_entrada(self, func):
        ''' Callback da interface gráfica: atualiza a view com os dados digitados e
        chama o modelo para criar a filmoteca. Após isto, exibe a filmoteca na view. '''

        # inicializa e cria filme
        self.filme = Filme()
        self.filme.titulo = self.view.titulo_entry.get()
        self.filme.ano = self.view.ano_entry.get()
        self.filme.nota = self.view.nota_entry.get()
        tup = self.view.lb.curselection()   # Pegar o item selecionado na listbox
        
        # executa um dos métodos do FilmotecaModel
        print(f'---------metodo {func} -------------')
        print(self.filme)
        
        if func == 'insere':
            self.model.inserir(self.filme)
        elif func == 'atualiza':
            if tup == ():
                print('Error: Clique no filme que deseja atualizar')
            else:
                indice = tup[0]
                self.model.atualizar(indice, self.filme)
        elif func == 'remove':
            if tup == ():
                print('Error: Clique no filme que deseja remover')
            else:
                indice = tup[0]
                self.model.remover(indice)
                print('indice:', indice)

        print('self.model._listaFilmes:', self.model._listaFilmes)
        self.view.v_lista_filmes.set(self.model._listaFilmes)
        

if __name__ == "__main__":

    # cria controller
    controller = FilmotecaController()

    # cria modelo
    model = FilmotecaModel()

    # cria view
    view = FilmotecaView(controller.root)

    # chama os métodos necessários do controller
    # para inicar a aplicação
    controller.inicializa(model, view)
    controller.executa()