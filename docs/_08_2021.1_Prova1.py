'''
POO 2021.1 - Prova 1
Implemente o sistema proposto a seguir, no qual um Usuario pode realizar um Pedido formado por vários Produto.

Diagrama de classes

Detalhes do sistema são dados como segue.

Classe Usuario
Atributos:

nome, encapsulado com get/set estilo Python (com @property)
cpf, encapsulado com get/set estilo Python (com @property)
Métodos:

__init__: não deve receber nenhum parâmetro (nome e cpf devem ser inicializados como None)
Classe Produto
Atributos:

codigo, encapsulado com get/set estilo Python (com @property)
preco, encapsulado com get/set estilo Python (com @property)
Um Produto é uma agregação de outros produtos similares a ele. Então, implemente o get (sem set) estilo Python para fornecer acesso à lista encapsulada de produtos similares fora da classe.

Métodos:

__init__: deve receber como parâmetros o seu código e preço
__str__: converte o produto para uma string no formato codigo - preco
Classe Pedido
Atributos:

numero (não precisa de get/set)
Observe a relação da classe Pedido com a classe Usuario e Produto e declare os atributos necessários para modelar as relações desejadas.

Métodos:

__init__: deve receber como parâmetro o número do pedido; inicialmente o produto não tem um usuário associado
associa_usuario: associa um usuário passado como parâmetro ao pedido
adiciona_produto: adiciona um Produto passado como parâmetro ao pedido
remove_produto: remove do pedido um Produto que tenha como código o int passado como parâmetro
mostra_similares: imprime todos os Produto similares ao Produto passado como parâmetro
imprime: imprime o Pedido no seguinte formato:
Usuario: <usuario.nome> (<usuario.cpf>) - Pedido <numero>
cod_prod1 - preco_prod1
...
cod_prodN - preco_prodN
Caso não tenha um usuário associado, o método deve imprimir

Usuario: usuário não logado - Pedido <numero>
cod_prod1 - preco_prod1
...
cod_prodN - preco_prodN
Utilize o código a seguir como ponto de partida.


Saída esperada:

Produto já adicionado ao pedido
Usuario: não logado - Pedido 10
1 - R$50.0
2 - R$150.0
3 - R$500.0
4 - R$130.0
5 - R$140.0
Produtos similares ao produto 2:
Código: 4
Código: 5
Usuario: não logado - Pedido 10
1 - R$50.0
2 - R$150.0
3 - R$500.0
Usuario: jose (111111) - Pedido 10
1 - R$50.0
2 - R$150.0
3 - R$500.0

'''

class Usuario:
    def __init__(self):
        self._nome = None
        self._cpf = None
        
    @property
    def nome(self):
        '''retorna o nome'''
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        '''muda o nome'''
        self._nome = novo_nome
        
    @property
    def cpf(self):
        '''retorna o cpf'''
        return self._cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        '''muda o cpf'''
        self._cpf = novo_cpf
        
    def __str__(self):
        return f'{self._nome} ({self._cpf})'

    
class Produto:
    def __init__(self, codigo, preco):
        self._codigo = codigo
        self._preco = preco
        self._similares = []
    
    @property
    def similares(self):
        '''retorna lista de produtos similares'''
        return self._similares
    
    def __str__(self):
        return f'{self._codigo} - {self._preco}'

    
class Pedido:
    def __init__(self, numero):
        self._numero = numero
        self._produtos = []
        self._usuario = None
    
    def associa_usuario(self, usuario):
        self._usuario = usuario
    
    def adiciona_produto(self, produto):
        if produto in self._produtos:
            print(f'Produto já adicionado ao pedido')
        else:
            self._produtos.append(produto)
    
    def remove_produto(self, cod):
        for p in self._produtos:
            if p._codigo == cod:
                self._produtos.remove(p)
                
    def mostra_similares(self, prod):
        print(f'Produtos similares ao produto {prod._codigo}:')
        for p in prod._similares:
            print(f'Código: {p._codigo}')
    
    def imprime(self):
        if self._usuario == None:
            print(f'Usuario: não logado - Pedido {self._numero}')
        else:
            print(f'Usuario: {self._usuario} - Pedido {self._numero}')
        for p in self._produtos:
            print(f'{p._codigo} - R${p._preco}')

if __name__ == '__main__':
    prod1 = Produto(1, 50.0)
    prod2 = Produto(2, 150.0)
    prod3 = Produto(3, 500.0)
    prod4 = Produto(4, 130.0)
    prod5 = Produto(5, 140.0)
    
    prod2.similares.append(prod4)
    prod2.similares.append(prod5)
    
    ped = Pedido(10)
    ped.adiciona_produto(prod1)
    ped.adiciona_produto(prod1)
    ped.adiciona_produto(prod2)
    ped.adiciona_produto(prod3)
    ped.adiciona_produto(prod4)
    ped.adiciona_produto(prod5)
    ped.imprime()
    ped.mostra_similares(prod2)
    ped.remove_produto(4)
    ped.remove_produto(5)
    ped.imprime()

    usuario = Usuario()
    usuario.nome = 'jose'
    usuario.cpf = 111111

    ped.associa_usuario(usuario)
    ped.imprime()
