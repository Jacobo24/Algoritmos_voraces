# Parejas

link al repositorio: 

Hay n parejas sentadas en 2n asientos dispuestos en fila y quieren darse la mano.
Las personas y los asientos están representados por un array de números enteros row
donde row[i] contiene el ID de la persona sentada en el asiento. Las parejas están
numeradas en orden, siendo la primera pareja (0,1), la segunda pareja (2,3), y así
sucesivamente hasta que la última pareja sea (2n - 2, 2n - 1)
Devuelve el número mínimo de intercambios para que cada pareja esté sentada una al lado
de la otra . Un intercambio consiste en elegir a dos personas cualesquiera, luego se
levantan y cambian de asiento.

Ejemplo 1:

Entrada -> row = [0,2,1,3]

Salida -> 1

Explicación: Solo necesitamos intercambiar la segunda (row[1]) y la
tercera (row[2]) persona.

Ejemplo 2:

Entrada -> row = [3,2,0,1]

Salida -> 0

Explicación: Todas las parejas ya están sentadas una al lado de la otra.
