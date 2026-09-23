import java.util.Random;

public class Arreglos {

    public static void main(String[] args) {
        int numAlumnos = 1000;
        int numMaterias = 1000;
        Random random = new Random();

        // Inicio de la medición del tiempo total de ejecución
        long inicioTiempo = System.nanoTime();

        // Declaración e inicialización de la matriz: [Alumno][Materia]
        double[][] matrizA = new double[numAlumnos][numMaterias];

        // Llenado de la matriz con calificaciones aleatorias de 5.0 a 10.0
        for (int i = 0; i < numAlumnos; i++) {
            for (int j = 0; j < numMaterias; j++) {
                matrizA[i][j] = 5.0 + (10.0 - 5.0) * random.nextDouble();
            }
        }

        System.out.println("=========================================================================");
        System.out.println("            TABLA DE CALIFICACIONES (500 ALUMNOS Y 6 MATERIAS)");
        System.out.println("=========================================================================\n");

        // Impresión del encabezado de la tabla
        System.out.println("+---------------+-----------+-----------+-----------+-----------+-----------+-----------+");
        System.out.println("| Alumno        | Mat. 1    | Mat. 2    | Mat. 3    | Mat. 4    | Mat. 5    | Mat. 6    |");
        System.out.println("+---------------+-----------+-----------+-----------+-----------+-----------+-----------+");

        // Imprime los 500 alumnos enumerados del 1 al 500
        for (int i = 0; i < numAlumnos; i++) {
            System.out.printf("| Alumno %-6d |", i + 1);
            for (int j = 0; j < numMaterias; j++) {
                System.out.printf(" %9.2f |", matrizA[i][j]);
            }
            System.out.println();
        }
        System.out
                .println("+---------------+-----------+-----------+-----------+-----------+-----------+-----------+\n");

        // Fin de la medición del tiempo de ejecución
        long finTiempo = System.nanoTime();

        // Conversión de nanosegundos a milisegundos
        double tiempoEjecucionMS = (finTiempo - inicioTiempo) / 1e6;

        System.out.println("-------------------------------------------------------------------------");
        System.out.printf("Tiempo total de ejecución del programa: %.4f ms\n", tiempoEjecucionMS);
        System.out.println("-------------------------------------------------------------------------");
    }
}