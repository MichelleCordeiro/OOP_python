import tkinter as tk
import tkinter.font as font

class FilmotecaView:
    '''View: interface gráfica Tkinter para filmoteca'''
    
    def __init__(self, root):
        self.root = root
        self.botoes = {}
        self.lista_filmes = []

        self._inicializa_gui()
    
    def _inicializa_gui(self):
        # customização
        textFont = font.Font(size=11)
        buttonFont = font.Font(size=10)
        self.root.resizable(False, False)   # não permitir redimencionamento
        
        # frame esquerdo
        frame_esq = tk.Frame(self.root, background="lightgray", bd=20, relief="sunken")
        frame_esq.grid(row=0, column=0, sticky="NSWE")
        
        # frame direito
        frame_dir = tk.Frame(self.root, background="lightgray", bd=20, relief="sunken")
        frame_dir.grid(row=0, column=1, sticky="NSWE")
        
        # configuração do redimensionamento do root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # itens lado esquerdo
        # entrada de texto
        self.titulo_label = tk.Label(frame_esq, text='Título:', anchor='w', padx=5, bg='lightgray', width=5)
        self.titulo_var = tk.StringVar()
        self.titulo_entry = tk.Entry(frame_esq, textvariable=self.titulo_var, width=12)
        
        self.ano_label = tk.Label(frame_esq, text='Ano:', anchor='w', padx=5, bg='lightgray', width=5)
        self.ano_label['font'] = textFont
        self.ano_var = tk.StringVar()
        self.ano_entry = tk.Entry(frame_esq, textvariable=self.ano_var, width=12)
        
        self.nota_label = tk.Label(frame_esq, text='Nota:', anchor='e', padx=15, bg='lightgray', width=5)
        self.nota_label['font'] = textFont
        self.nota_var = tk.StringVar()
        self.nota_entry = tk.Entry(frame_esq, textvariable=self.nota_var, width=12)
        
        # configuração do tamanho das fontes das labels e entrys
        self.titulo_label['font'] = textFont
        self.titulo_entry['font'] = textFont
        self.ano_label['font'] = textFont
        self.ano_entry['font'] = textFont
        self.nota_label['font'] = textFont
        self.nota_entry['font'] = textFont
        
        # configuração do posicionamento das labels e entrys
        self.titulo_label.grid(row=0, column=0)
        self.titulo_entry.grid(row=0, column=1, columnspan=4, sticky='WE')
        self.ano_label.grid(row=1, column=0)
        self.ano_entry.grid(row=1, column=1, sticky='WE')
        self.nota_label.grid(row=1, column=2)
        self.nota_entry.grid(row=1, column=3, sticky='WE')

        # botões
        self.botoes['Insere'] = tk.Button(frame_esq, text="Insere")
        self.botoes['Insere']['font'] = buttonFont
        self.botoes['Atualiza'] = tk.Button(frame_esq, text="Atualiza")
        self.botoes['Atualiza']['font'] = buttonFont
        self.botoes['Remove'] = tk.Button(frame_esq, text="Remove")
        self.botoes['Remove']['font'] = buttonFont
                
        # configuração do posicionamento dos botões        
        self.botoes['Insere'].grid(row=2, column=1, sticky="WE")
        self.botoes['Atualiza'].grid(row=2, column=2, sticky="WE")
        self.botoes['Remove'].grid(row=2, column=3, sticky="WE")
        #self.bt_insere.grid(row=2, column=1, sticky="WE")
        #self.bt_atualiza.grid(row=2, column=2, sticky="WE")
        #self.bt_remove.grid(row=2, column=3, sticky="WE")
        
        # itens lado direito
        # listbox
        self.v_lista_filmes = tk.StringVar()
        self.lb = tk.Listbox(frame_dir, listvariable=self.v_lista_filmes, bd=0, width=45, height=30, bg="white", cursor="hand2")
        self.lb['font'] = textFont
        
        # configuração do posicionamento do listbox        
        self.lb.grid(row=0, column=0, sticky='NSWE')
        
        # Scrollbars da listbox
        scrollbar_y = tk.Scrollbar(frame_dir, orient='vertical', command=self.lb.yview)
        scrollbar_x = tk.Scrollbar(frame_dir, orient='horizontal', command=self.lb.xview)
        
        # configuração do posicionamento das scrollbars       
        self.lb['yscrollcommand'] = scrollbar_y.set
        self.lb['xscrollcommand'] = scrollbar_x.set
        scrollbar_y.grid(row=0, column=1, sticky='NSWE')
        scrollbar_x.grid(row=1, column=0, sticky='NSWE')
        
        
if __name__ == "__main__":

    # cria janela Tk para teste
    root = tk.Tk()
    root.geometry('800x600')
    root.title('Teste GUI')

    # instancia o view
    f = FilmotecaView(root)

    tk.mainloop()
    