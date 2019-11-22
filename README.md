# Algoritmos de búsqueda

Recuperar información de una computadora es una de las actividades más útiles e 
importantes, muy comúnmente se tiene un nombre o llave que se quiere encontrar en 
una estructura de datos tales como una lista u arreglo.

Al proceso de encontrar un dato específico llamado llave en alguna estructura de 
datos, se denomina **búsqueda**. Este proceso termina exitosamente cuando se localiza 
el elemento que contienen la llave buscada, o termina sin éxito, cuando no aparece 
ningún elemento con esa llave.

Los algoritmos de búsqueda se pueden clasificar en:
- Búsqueda por comparación (lineal o secuencial y binaria)
- Búsqueda por transformación de llaves.

## Búsqueda por comparación (lineal o secuencial y binaria)

### Búsqueda lineal

En este algoritmo se empieza a buscar desde la primera posición de la lista, comparando 
el elemento con la llave y si no se encuentra continúa verificando las siguientes posiciones 
hasta encontrarlo, entonces el algoritmo termina. Así el elemento a buscar puede estar en el 
primer elemento, el último o entre ellos.

A continuación, se muestra un algoritmo en pseudocódigo de una función que realiza la búsqueda 
secuencial del elemento *x* en una lista implementada como un arreglo lineal *A[0, 1, 2, … n − 1]* 
de *n* elementos. El cual retorna la posición o índice del arreglo donde se encuentra el elemento *x* 
a buscar, y el valor de −1 si *x* no fue encontrado.

```
BúsquedaLineal (A,n,x )
Inicio
    encontrado=-1
    Para k=0 hasta n-1
        Si x==A[k]
            encontrado = k
        Fin Si
    Fin Para
    Retorna encontrado
Fin
```

Como se puede observar en la función BúsquedaLineal(), el número de iteraciones siempre es igual al tamaño 
del arreglo *A*, independientemente de dónde se encuentre el elemento a buscar y como todas las operaciones 
del interior de la estructura de repetición tienen una complejidad constante, la complejidad de este algoritmo 
de búsqueda secuencial es de **O(n)**.

Existen varias mejoras al algoritmo, una de ellas es no esperar a revisar todos los elementos del arreglo, 
si el buscado ya se encontró, entonces se tiene que terminar. Una forma de conseguirlo es revisar en cada 
iteración *k*, si el elemento a buscar *x* es ya igual al elemento *A[K]*, y si lo es, entonces retornar la 
posición del elemento encontrado y terminar. A continuación, se muestra una posible función en pseudocódigo 
donde se considera esta mejora.

```
BúsquedaLinealMejorado
Inicio
    encontrado=-1
    Para k=0 hasta n-1
        Si A[k]==x
            encontrado= k
            Salir de la estructura de repetición
        Fin Si
    Fin Para
    retorna encontrado
Fin
```

### Búsqueda binaria

El algoritmo de búsqueda binaria es eficiente para encontrar un elemento en una lista ya ordenada y es un 
ejemplo de la técnica divide y conquista. 

Entonces en el algoritmo se divide repetidamente a la mitad la porción de la lista que podría contener al 
elemento, hasta reducir las ubicaciones posibles a solo una. La estrategia consiste en comparar una llave 
con el elemento de en medio de la lista, si es igual entonces se encontró el elemento, sino, cuando *x* es 
menor que el elemento del medio se aplica la misma estrategia a la lista de la izquierda y si *x* es mayor, 
a la lista de la derecha.

Para describir el algoritmo con más detalle, se supone una la lista ordenada de forma ascendente que está 
almacenada en un arreglo unidimensional *A[0,…,n−1]* de *n* elementos y se quiere encontrar la llave *x*.

1. Primero se calcula el índice del punto medio del arreglo utilizando los índices de inicio (izquierdo) 
y fin (derecho) de la lista o sublista de búsqueda, *medio = |(índiceIzquierdo+índiceDerecho) / 2|*, para 
poder dividir la lista en dos sub-listas.
2. Después se compara el punto *medio* con la llave a buscar *x*,
- Si son iguales, entonces la llave fue encontrada, y el algoritmo termina.
- Si el valor del arreglo *A* con índice *medio* es mayor a la llave *x(A[medio] > x)*, se descarta la 
sub-lista de la derecha incluyendo el punto *medio* y se regresa al paso 1, donde la nueva sub-lista de 
búsqueda mantiene el índice izquierdo y el índice derecho cambia a *medio*.
- Si el valor del arreglo *A* con índice medio es menor a la llave *x(A[medio] < x)*, se descarta la 
sub-lista de la izquierda incluyendo el punto medio y se regresa al paso 1, donde la nueva sub-lista de 
búsqueda mantiene el índice derecho y el índice izquierdo cambia a *medio*.

Si en algún momento la sub-lista de búsqueda tiene longitud 0 o negativa significa que el valor buscado 
no se encuentra en la lista.

Una función del algoritmo en pseudocódigo de la búsqueda binaria descrita es:

```
BusquedaBinariaIterativa(A, x, indiceIzq, indiceDer)
Inicio
    Encontrado = -1
    Mientras indiceIzq <= indiceDer
        Medio=>[(indiceIzq + indiceDer) / 2]
            Si x == A[Medio] entonces
                Encontrado=Medio
            Si no
                Si A[medio] < x
                    indiceIzq=medio +1
                Si no
                    indiceDer=medio-1
                Fin Si no
            Fin Si no
    Fin Mientras
    Retorna Encontrado
Fin
```

El pseudocódigo retorna la posición donde se encuentra el elemento o bien −1 si no se encuentra. El 
tiempo de ejecución es **0(log n)**.

Cormen, T. (2013). Algorithms Unlocked. Cambridge: IT Press.