import tkinter as tk

class Calculadora:
    def __init__(self):        
        self.num1 = None
        self.num2 = None
        self.res = None
    
    def operacao(self, op):
        if op == '+':
            self.res = self.num1 + self.num2
            return self.res
        if op == '-':
            self.res = self.num1 - self.num2
            return self.res
        if op == '*':
            self.res = self.num1 * self.num2
            return self.res
        
        
class CalculadoraGUI:
    def __init__(self):
        self.calculadora = Calculadora()
        self.estado = 'num1'
        self.op = None
        self.bt_op = {}

        # janela principal
        self.root = tk.Tk()
        self.root.title('Calculadora TK')
        self.root.geometry('400x400+50+500')
        self.root.resizable(False, False)   # não permite redimencionamento da janela
        
        self._inicializa_variaveis()
        self._inicializa_gui()
        tk.mainloop()

    def _inicializa_variaveis(self):
        self.var_texto = tk.StringVar()
        
    def _inicializa_gui(self):
        # frame interno
        frame1 = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        frame1.pack(expand=True, fill=tk.BOTH)

        # Display da calculadora
        entry_texto = tk.Entry(frame1, textvariable=self.var_texto)
        entry_texto.pack(side=tk.TOP, fill=tk.X)
        
        # frame dos botões
        frame2 = tk.Frame(frame1, bd=5, relief=tk.SUNKEN, bg='gray')
        frame2.pack(expand=True, fill=tk.BOTH)

        # botões
        b7 = tk.Button(frame2, text='7', bg='lightgray', command=lambda:self._processa_clicks(7))
        b8 = tk.Button(frame2, text='8', bg='lightgray', command=lambda:self._processa_clicks(8))
        b9 = tk.Button(frame2, text='9', bg='lightgray', command=lambda:self._processa_clicks(9))
        b4 = tk.Button(frame2, text='4', bg='lightgray', command=lambda:self._processa_clicks(4))
        b5 = tk.Button(frame2, text='5', bg='lightgray', command=lambda:self._processa_clicks(5))
        b6 = tk.Button(frame2, text='6', bg='lightgray', command=lambda:self._processa_clicks(6))
        b1 = tk.Button(frame2, text='1', bg='lightgray', command=lambda:self._processa_clicks(1))
        b2 = tk.Button(frame2, text='2', bg='lightgray', command=lambda:self._processa_clicks(2))
        b3 = tk.Button(frame2, text='3', bg='lightgray', command=lambda:self._processa_clicks(3))
        b0 = tk.Button(frame2, text='0', bg='lightgray', command=lambda:self._processa_clicks(0))

        self.bt_op['+'] = tk.Button(frame2, text='+', bg='lightgray', command=lambda:self._processa_clicks('+'))
        self.bt_op['-'] = tk.Button(frame2, text='-', bg='lightgray', command=lambda:self._processa_clicks('-'))
        self.bt_op['*'] = tk.Button(frame2, text='*', bg='lightgray', command=lambda:self._processa_clicks('*'))
        self.bt_op['='] = tk.Button(frame2, text='=', bg='lightgray', command=lambda:self._processa_clicks('='))
        
        # posicionamento dos botões
        b7.grid(row=0, column=0, sticky='NSWE')
        b8.grid(row=0, column=1, sticky='NSWE')
        b9.grid(row=0, column=2, sticky='NSWE')
        b4.grid(row=1, column=0, sticky='NSWE')
        b5.grid(row=1, column=1, sticky='NSWE')
        b6.grid(row=1, column=2, sticky='NSWE')
        b1.grid(row=2, column=0, sticky='NSWE')
        b2.grid(row=2, column=1, sticky='NSWE')
        b3.grid(row=2, column=2, sticky='NSWE')
        b0.grid(row=3, columnspan=2, sticky='NSWE')
        
        self.bt_op['+'].grid(row=0, column=3, sticky='NSWE')
        self.bt_op['-'].grid(row=1, column=3, sticky='NSWE')
        self.bt_op['*'].grid(row=2, column=3, sticky='NSWE')
        self.bt_op['='].grid(row=3, column=2, columnspan=2, sticky='NSWE')

        # posicionamento dos botões
        frame2.rowconfigure(0, weight=1)
        frame2.rowconfigure(1, weight=1)
        frame2.rowconfigure(2, weight=1)
        frame2.rowconfigure(3, weight=1)
        frame2.columnconfigure(0, weight=1)
        frame2.columnconfigure(1, weight=1)
        frame2.columnconfigure(2, weight=1)
        frame2.columnconfigure(3, weight=1)
        

    def _processa_clicks(self, par):
        # primeiro digito
        if self.estado == 'num1':
            if type(par) == int:
                self.var_texto.set(self.var_texto.get() + str(par))
            else:
                conteudo = self.var_texto.get()
                if conteudo.isdigit():
                    self.op = par
                    self.calculadora.num1 = int(conteudo)
                    self.estado = 'num2'
                    self.var_texto.set('')
                    self.bt_op[self.op]['relief'] = tk.SUNKEN

        # segundo digito
        elif self.estado == 'num2':
            if type(par) == int:
                self.var_texto.set(self.var_texto.get() + str(par))
            else:
                conteudo = self.var_texto.get()
                if conteudo.isdigit():
                    self.calculadora.num2 = int(conteudo)
                    self.calculadora.operacao(self.op)
                    self.var_texto.set(str(self.calculadora.res))
                    self.bt_op[self.op]['relief'] = tk.RAISED
                    self.estado = 'res_ok'

        elif self.estado == 'res_ok':
            if type(par) == int:
                self.var_texto.set(str(par))
                self.estado = 'num1'
                    

if __name__ == "__main__":
    c = CalculadoraGUI()