class Matriz:
    '''Representa uma matriz de tamanho nl x nc.'''

    def __init__(self, nl, nc):
        self._nl = nl
        self._nc = nc
        self._dados = []
        self._inicializa()

    def _inicializa(self):
        '''Inicializa a matriz com 0s.'''
        for i in range(self._nl):
            self._dados.append([])
            for j in range(self._nc):
                self._dados[i].append(0.0)

    def __repr__(self):
        '''Retorna a matriz em formato de str''' 
        s = ''
        for i in range(self._nl):
            for j in range(self._nc):
                s += f'{self._dados[i][j]} '
            s += '\n'
        return s

    def seta_valores(self, valores):
        '''Atribui valores em lista de listas à matriz.'''
        if len(valores) != self._nl or len(valores[0]) != self._nc:
            print('Lista de valores com tamanho incompatível')
        else:
            for i, lin in enumerate(valores):
                for j, v in enumerate(lin):
                    self._dados[i][j] = v
    
    def _checa_dimensoes(self, b, op):
        '''Retorna falso se as dimensões da matriz não são
           compatíveis com as dimensões do parâmetro b, de
           acordo com a op (soma ou multiplicação) desejada.
        '''
        if op == '+':
            if b._nl != self._nl or b._nc != self._nc:
                return False
        else:
            if self._nc != b._nl:
                return False
        return True
    
    def __getitem__(self, pos):
        '''Operador []: permite acessar
           um elemento da matriz através de m[i,j].
        '''
        #print(type(pos))
        if type(pos) == tuple:
            lin, col = pos
            if lin >= self._nl or col >= self._nc:
                print('excede a matriz')
            else:
                return self._dados[lin][col]
        else:
            print('pos deve ser tupla')

    def __setitem__(self, pos, v):
        '''Operador []: permite atribuir um valor
           a um elemento da matriz através de m[i,j].
        '''
        if type(pos) == tuple:
            lin, col = pos
            if lin >= self._nl or col >= self._nc:
                print('excede a matriz')
            else:
                self._dados[lin][col] = v
        else:
            print('pos deve ser tupla')

    def __add__(self, b):
        '''Operador +'''
        if not self._checa_dimensoes(b, '+'):
            print('Matriz passada por parâmetro não possuir dimensões compatíveis')
        else:
            soma_mat = Matriz(self._nl, self._nc)
            for i in range(self._nl):
                for j in range(self._nc):                    
                    soma_mat[i,j] = self[i,j] + b[i,j]
            return soma_mat
            
    def __mul__(self, b):
        '''Operador *'''
        if isinstance(b, Matriz):
            if self._checa_dimensoes(b, '*'):
                prod_mat = Matriz(self._nl, b._nc)
                for i in range(self._nl):
                    for j in range(b._nc):
                        for k in range(self._nc):
                            #prod_mat[i,j] = self[i,k] + (self[i,k] * b[k,j])
                            prod_mat[i,j] += self[i,k] * b[k,j]
                return prod_mat
        else:
            prod_mat_esc = Matriz(self._nl, self._nc)
            for i in range(self._nl):
                for j in range(self._nc):
                    prod_mat_esc[i,j] = (self[i,j] * b)
            return prod_mat_esc

    def __eq__(self, b):
        '''Operador =='''
        if self._nl != b._nl or self._nc != b._nc:
            return False
        else:
            for i in range(self._nl):
                for j in range(self._nc):
                    if self[i,j] != b[i,j]:
                        return False
        return True
    
    def __ne__(self, b):
        '''Operador !='''
        if self._nl != b._nl or self._nc != b._nc:
            return True
        for i in range(self._nl):
                for j in range(self._nc):
                    if self[i,j] != b[i,j]:
                        return True
        return False

if __name__ == "__main__":
    a = Matriz(3, 3)
    a[0,2] = 1
    a[1,1] = 1
    a[2,0] = 1
    print('Matriz a:')
    print(a)

    b = Matriz(3, 3)
    b.seta_valores([[1.0, 2.0, 0.0],
                    [2.0, 4.0, 5.0],
                    [3.0, 3.0, 0.0]])
    
    mat_soma = a + b
    print('A + B:')
    print(mat_soma)

    mat_prod = a * b
    print('A * B:')
    print(mat_prod)

    mat_prod = b * 5
    print('B * escalar:')
    print(mat_prod)

    print(f'A != B: {a!=b}')
    b.seta_valores([[0, 0, 1],
                    [0, 1, 0],
                    [1, 0, 0]])
    print(f'A == B: {a==b}')
