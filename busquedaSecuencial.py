class BusquedaSecuencial:
    def busqueda(self, lista, clave):
        """ Búsqueda lineal.
            Si clave está en lista devuelve True, de lo
            contrario devuelve False.
        """
        # Estrategia: se recorren uno a uno los elementos de la lista
        # y se los compara con el valor "clave" buscado.

        # encontrado tiene False si clave no es encontrado, True si clave
        # es encontrado, comienza en False
        encontrado = False
        # el ciclo for recorre todos los elementos de lista:
        for i in lista:
            # i contiene el valor de lista[i]

            # si i es igual a clave, devuelve True
            if i == clave:
                encontrado = True
                break
        # si salió del ciclo sin haber encontrado el valor, devuelve False
        return encontrado

    def busquedaLineal(self, lista, clave):
        """ Búsqueda lineal.
            Si x está en lista devuelve su posición en lista, de lo
            contrario devuelve -1.
        """
        # Estrategia: se recorren uno a uno los elementos de la lista
        # y se los compara con el valor x buscado.

        # i tiene la posición actual en la lista, comienza en 0
        i = 0

        # el ciclo for recorre todos los elementos de lista:
        for z in lista:
            # estamos en la posicion i, z contiene el valor de lista[i]
            # si z es igual a x, devuelve i
            if z == clave:
                return i
            # si z es distinto de x, incrementa i, y continúa el ciclo
            i = i + 1
        # si salió del ciclo sin haber encontrado el valor, devuelve -1
        return -1


def main():
    A = [9,3,1,4,5,7,7,2,20]
    b = BusquedaSecuencial()
    print(b.busquedaLineal(A, 7))

if __name__ == "__main__":
    main()
