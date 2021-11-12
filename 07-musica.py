class Musica:
    
    def __init__(self, artista, titulo):
        self._artista = artista
        self._titulo = titulo
        
    def __str__(self):
        return f'{self._artista} - {self._titulo}'