def main():

    musica = [('Yellou Mariene', 'The Beatles', 9.2), #Una lista constituida por tuplas
              ('Imagine', 'Jhon Lennon', 8.5),
              ('Let ib be', 'The Beatles', 9.0),
              ('Bohemian Rhapsody', 'Queen', 7.8),
              ('Stairway to Heaven', 'Let Zeppelin', 7.5)
              ]
    
    def buscar_cancion(nombre):
        for cancion in musica:
            if cancion[0] ==  nombre: #Se busca la posicion 0 porque es la de la tupla
                return (cancion) #si cancion es igual al nombre, retorna la cancion 
        return (None) #si no, no retorna nada
    
    def buscar_artista(artista):
        canciones_artista = []
        for cancion in musica:
            if cancion[1] ==  artista: 
                canciones_artista.append(cancion)
        return (canciones_artista) 
    
    print(buscar_cancion('Imagine'))
    print(buscar_artista('The Beatles'))

if __name__ == ("__main__"):
    main()