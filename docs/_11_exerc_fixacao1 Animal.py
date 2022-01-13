from abc import ABC, abstractmethod

class Animal(ABC):
    '''Classe abstrata Animal'''
    @abstractmethod
    def __init__(self, anim):
        self._anim = anim
    
    def nasce(self):
        pass
    
    def morre(self):
        pass
    
    def emite_som(self):
        return f'{self.__class__.__name__} {self._anim}'
    
    def __str__(self):
        return f'\n{self.__class__.__name__} {self._anim}'


class Mamifero(Animal):
    '''Classe abstrata Manifero'''
    @abstractmethod
    def __init__(self, anim):
        super().__init__(anim)
    
    def nasce(self):
        print('Nasce filhote')
    
    def amamenta(self):
        pass


class Gato(Mamifero):
    '''Classe concreta Gato'''
    def __init__(self, anim):
        super().__init__(anim)
    
    def emite_som(self):
        s = Animal.emite_som(self)
        s += ': mia'
        print(s)

class Cachorro(Mamifero):
    '''Classe concreta Cachorro'''
    def __init__(self, anim):
        super().__init__(anim)
    
    def emite_som(self):
        s = Animal.emite_som(self)
        s += ': late'
        print(s)

class Ornitorrinco(Mamifero):
    '''Classe concreta Ornitorrinco'''
    def __init__(self, anim):
        super().__init__(anim)
    
    def nasce(self):
        print('Põe ovo')
    
    def emite_som(self):
        s = Animal.emite_som(self)
        s += ': quac (pq tem bico de pato kkk)'
        print(s)


class Ave(Animal):
    '''Classe abstrata Ave'''
    @abstractmethod
    def __init__(self, anim):
        super().__init__(anim)
        
    def nasce(self):
        print('Põe ovo')
    
    def voa(self):
        print('Sim, voa')
        
    def emite_som(self):
        s = Animal.emite_som(self)
        s += ': pia'
        print(s)

class Pinguim(Ave):
    '''Classe concreta Pinguim'''
    def __init__(self, anim):
        super().__init__(anim)
        
    def voa(self):
        print('Não voa')
        
class Aguia(Ave):
    '''Classe concreta Aguia'''
    def __init__(self, anim):
        super().__init__(anim)
        
        
if __name__ == "__main__":

    #test = Animal('gatinho')
    #test = Mamifero('gatinho')
    
    a1 = Gato('persa')
    print(a1)
    a1.nasce()
    a1.morre() #não implementado
    a1.emite_som()
    a1.amamenta()  #não implementado
    
    a2 = Ornitorrinco('qq coisa')
    print(a2)
    a2.nasce()
    a2.morre() #não implementado
    a2.emite_som()
    a2.amamenta()  #não implementado
    
    a3 = Pinguim('imperial')
    print(a3)
    a3.nasce()
    a3.morre() #não implementado
    a3.emite_som()
    a3.voa()
    #a3.amamenta()  #testando
    
    a4 = Aguia('careca')
    print(a4)
    a4.nasce()
    a4.morre() #não implementado
    a4.emite_som()
    a4.voa()