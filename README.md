# Estructura

#Programa EjerArreglo 
En este ejercicio hice un programa en Java para organizar las ventas mensuales de tres áreas distintas: Ropa, Deportes y Juguetería, abarcando los 12 meses del año.

Para guardar la información usé una matriz bidimensional de tipo double de 12 filas por 3 columnas:

Las 12 filas son para los meses del año (donde Enero es la posición 0 y Diciembre la 11).

Las 3 columnas corresponden a cada departamento: Ropa en la posición 0, Deportes en la 1 y Juguetería en la 2.

¿Cómo funcionan el menú y los métodos?

Para interactuar con el programa armé un menú en consola que usa la clase Scanner para pedir los datos. El código incluye los siguientes métodos:

cargarDatosIniciales()
Este método lo puse para que la matriz no empiece vacía. Le asigna montos reales y mayores a cero a cada mes y departamento desde que arranca el programa.

insertarVentaConScanner(Scanner scanner)
Sirve para registrar o modificar una venta. Te despliega la lista de meses y departamentos con sus números para que selecciones la posición exacta y luego te pide ingresar el monto por teclado para guardarlo en la matriz.

buscarVentaConScanner(Scanner scanner)
Te pide un monto a buscar y recorre toda la matriz con dos ciclos for. Si encuentra esa cantidad guardada, te dice exactamente en qué mes y departamento está registrada.

eliminarVentaConScanner(Scanner scanner)
Te pide seleccionar el mes y el departamento de la venta que quieres quitar. Como los arreglos en Java no se pueden encoger, lo que hace es cambiar el valor de esa casilla a 0.0 para simular la eliminación.

mostrarTabla()
Muestra en pantalla toda la matriz ordenada en filas y columnas para que sea fácil ver las ventas registradas.
