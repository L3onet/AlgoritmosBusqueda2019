class BusquedaSecuencial:
    def busqueda(self, lista, clave):
        encontrado = False
        for i in range(0, len(lista), 1):
            if lista[i] == clave:
                encontrado = True
                break
        return encontrado

def main():
    A = [9,3,1,4,5,7,7,2,20]
    b = BusquedaSecuencial()
    print(b.busqueda(A, 7))

if __name__ == "__main__":
    main()
