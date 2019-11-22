import math

class BusquedaBinaria:
    def Busqueda(self, lista, clave, izquierda, derecha):
        """Búsqueda binaria
            Precondición: lista está ordenada
            Devuelve -1 si clave no está en lista;
            Devuelve p tal que lista[p] == clave, si clave está en lista
            """

        # Busca en toda la lista dividiéndola en segmentos y considerando
        # a la lista completa como el segmento que empieza en 0 y termina
        # en len(lista) - 1.

        # izquierda guarda el índice inicio del segmento
        # derecha guarda el índice fin del segmento

        while izquierda <= derecha:
            # el punto medio del segmento
            medio = math.floor((izquierda + derecha) / 2)
            # si el medio es igual al valor buscado, lo devuelve
            if lista[medio] == clave:
                return medio
            # si el valor del punto medio es menor que clave, sigue buscando
            # en el segmento de la derecha: [medio+1, der],
            # descartando la izquierda
            elif lista[medio] < clave:
                izquierda = medio + 1
            # sino, sigue buscando en el segmento de la izquierda: [izq, medio-1],
            # descartando la derecha
            else:
                derecha = medio - 1
            # si no salió del ciclo, vuelve a iterar con el nuevo segmento

        # salió del ciclo de manera no exitosa: el valor no fue encontrado
        return -1

def main():
    A = [1,2,3,4,5,7,7,9,20]
    b = BusquedaBinaria()
    print(b.Busqueda(A, 7, 0, len(A)-1))

if __name__ == "__main__":
    main()