import random
    
class Playlist:
    
    def __init__(self, musicas):
        self._musicas = musicas
    
    def imprime(self):
        if len(self._musicas) > 0:
            l = f' ----------------'
            for m in self._musicas:
                l += f'\n {m}'
            l += 'f\n ----------------'
            print(l)
        
    def adiciona(self, musica):
        self._musicas.append(musica)
    
    def toca_proxima(self):
        if len(self._musicas) > 0:
            print(f' Tocando agora: {self._musicas[0]}')
            self._musicas.remove(self._musicas[0])
        else:
            print(' Sua playlist chegou ao fim')      
    
    def embaralha(self):
        random.shuffle(self._musicas)