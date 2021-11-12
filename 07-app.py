from musica import Musica
from playlist import Playlist


m1 = Musica('Nirvana', 'Smells Like Teen Spirit')
m2 = Musica('Green Day', 'Basket Case')
m3 = Musica('The Offspring', 'Original Prankster')
m4 = Musica('Foo Fighters', 'Everlong')
m5 = Musica('Avril Lavigne', 'Skater Boy')
m6 = Musica('Papa Roach', 'Last Resort')
musicas = [m1, m2, m3]

pl = Playlist(musicas)
pl.imprime()

pl.adiciona(m4)
pl.imprime()

pl.toca_proxima()
pl.toca_proxima()
pl.imprime()

pl.adiciona(m5)
pl.adiciona(m6)
pl.embaralha()
pl.imprime()