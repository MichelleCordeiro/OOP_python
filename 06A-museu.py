''' Prática 3a: Museu e Obras de Arte
Defina a classe Obra para representar uma obra de arte, com os seguintes atributos:

Nome
Autor
Ano
O único método da classe é o __str__, que deve imprimir o nome, autor e ano da obra. Não precisa de getters/setters.

Defina também a classe Museu, que deve conter uma agregação de obras de arte entre os seus atributos, além do seu nome. Os seus métodos devem ser:

adiciona_obra: adiciona objeto da classe Obra à sua agregação
remove_obra: remove da sua agregação uma Obra que tenha como nome a string passada como parâmetro
imprime_obras: imprime todas as obras da sua agregação
Utilize o código base a seguir como ponto de partida.


Resultado esperado:

Obras do museu "museu magnifico":
    mona lisa, da vinci (1797)
    a noite estrelada, van gogh (1889)
    guernica, picasso (1937)
    a persistencia da memoria, dali (1931)
Obras do museu "museu magnifico":
    mona lisa, da vinci (1797)
    a noite estrelada, van gogh (1889)
    a persistencia da memoria, dali (1931)
Obra removida:
guernica, picasso (1937)
'''
class Obra:
    '''Uma obra'''
    
    def __init__(self, nome, autor, ano):
        self._nome = nome 
        self._autor = autor
        self._ano = ano
    
    def __str__(self):
        return f'{self._nome}, {self._autor} ({self._ano})'
    
    
class Museu:
    '''Um museu'''
    
    def __init__(self, nome):
        self._nome = nome
        self._obras = []
        
    def adiciona_obra(self, obra):
        '''Adiciona obra'''
        self._obras.append(obra)
        #for obra in self._obras:
            #print(obra)
    
    def imprime_obras(self):
        '''Imprime obras'''
        print(f'Obras do museu "{self._nome}":')
        for o in self._obras:
            print(f'    {o}')
    
    def remove_obra(self, obra):
        '''Remove obra'''
        for o in self._obras:            
            #print("obra:", obra)
            #print("1 - o:", o)
            if o._nome == obra:
                self._obras.remove(o)
    

if __name__ == '__main__':
    # cria obras
    o1 = Obra('mona lisa', 'da vinci', 1797)
    o2 = Obra('a noite estrelada', 'van gogh', 1889)
    o3 = Obra('guernica', 'picasso', 1937)
    o4 = Obra('a persistencia da memoria', 'dali', 1931)

    # cria museu
    m = Museu('museu magnifico')

    # adiciona obras criadas ao museu
    m.adiciona_obra(o1)
    m.adiciona_obra(o2)
    m.adiciona_obra(o3)
    m.adiciona_obra(o4)

    # imprime obras
    m.imprime_obras()

    # remove obras do museu
    m.remove_obra('a ultima ceia') # nao faz nada
    m.remove_obra('guernica')

    # imprime obras
    m.imprime_obras()

    # obra continua a existir mesmo tendo sido removida do museu
    print('Obra removida:')
    print(o3)
