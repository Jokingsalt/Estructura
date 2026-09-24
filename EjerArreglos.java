import java.util.Scanner;

public class EjerArreglos {

    private double[][] ventas;
    private String[] meses = { "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" };
    private String[] departamentos = { "Ropa", "Deportes", "Juguetería" };

    // Constructor con el nombre correcto de la clase
    public EjerArreglos() {
        // Matriz de 12 filas (meses) y 3 columnas (departamentos)
        ventas = new double[12][3];
        // Inicializamos la tabla con valores diferentes de 0
        cargarDatosIniciales();
    }

    // Método para rellenar la tabla con valores base (todos mayores a 0)
    private void cargarDatosIniciales() {
        double[][] datosBase = {
                { 1200.50, 2100.00, 1500.00 }, // Enero
                { 1350.00, 1950.00, 1100.00 }, // Febrero
                { 1500.00, 2300.00, 1400.00 }, // Marzo
                { 1100.25, 2050.00, 1800.50 }, // Abril
                { 1750.00, 2400.00, 1650.00 }, // Mayo
                { 1900.00, 2800.00, 1900.00 }, // Junio
                { 2100.00, 3100.00, 2200.00 }, // Julio
                { 1600.00, 2500.00, 1750.00 }, // Agosto
                { 1450.00, 2200.00, 1300.00 }, // Septiembre
                { 1800.00, 2600.00, 2000.00 }, // Octubre
                { 2200.00, 3400.00, 2800.00 }, // Noviembre
                { 3500.00, 4800.00, 5200.00 } // Diciembre
        };

        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 3; j++) {
                ventas[i][j] = datosBase[i][j];
            }
        }
    }

    // 1. Método para insertar o modificar un elemento con Scanner
    public void insertarVentaConScanner(Scanner scanner) {
        System.out.println("\n--- REGISTRAR / MODIFICAR VENTA ---");

        System.out.println("Seleccione el mes:");
        for (int i = 0; i < meses.length; i++) {
            System.out.println("[" + i + "] " + meses[i]);
        }
        System.out.print("Ingrese el número de mes (0-11): ");
        int mes = leerEnteroValido(scanner, 0, 11);

        System.out.println("\nSeleccione el departamento:");
        for (int j = 0; j < departamentos.length; j++) {
            System.out.println("[" + j + "] " + departamentos[j]);
        }
        System.out.print("Ingrese el número de departamento (0-2): ");
        int depto = leerEnteroValido(scanner, 0, 2);

        System.out.print("\nIngrese el nuevo monto para " + meses[mes] + " en " + departamentos[depto] + ": $");
        while (!scanner.hasNextDouble()) {
            System.out.print("Valor inválido. Ingrese un monto numérico: $");
            scanner.next();
        }
        double monto = scanner.nextDouble();

        ventas[mes][depto] = monto;
        System.out.println(" ¡Venta actualizada con éxito!\n");
    }

    // 2. Método para buscar un elemento en particular con Scanner
    public void buscarVentaConScanner(Scanner scanner) {
        System.out.print("\n--- BUSCAR VENTA ---\nIngrese el monto de la venta a buscar: $");

        while (!scanner.hasNextDouble()) {
            System.out.print("Por favor, ingrese un monto numérico válido: $");
            scanner.next();
        }

        double montoBuscado = scanner.nextDouble();
        boolean encontrado = false;

        System.out.println("Buscando ventas por $" + montoBuscado + "...");

        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 3; j++) {
                if (ventas[i][j] == montoBuscado) {
                    System.out.println("-> Encontrado en " + meses[i] + " (" + departamentos[j] + ")");
                    encontrado = true;
                }
            }
        }

        if (!encontrado) {
            System.out.println("No se encontró ninguna venta registrada por $" + montoBuscado);
        }
        System.out.println();
    }

    // 3. Método para eliminar una venta en particular
    public void eliminarVentaConScanner(Scanner scanner) {
        System.out.println("\n--- ELIMINAR VENTA ---");

        System.out.println("Seleccione el mes:");
        for (int i = 0; i < meses.length; i++) {
            System.out.println("[" + i + "] " + meses[i]);
        }
        System.out.print("Ingrese el número de mes (0-11): ");
        int mes = leerEnteroValido(scanner, 0, 11);

        System.out.println("\nSeleccione el departamento:");
        for (int j = 0; j < departamentos.length; j++) {
            System.out.println("[" + j + "] " + departamentos[j]);
        }
        System.out.print("Ingrese el número de departamento (0-2): ");
        int depto = leerEnteroValido(scanner, 0, 2);

        ventas[mes][depto] = 0.0;
        System.out.println(
                " ¡La venta de " + meses[mes] + " en " + departamentos[depto] + " ha sido restablecida a $0.0!\n");
    }

    // Método auxiliar para validar el rango de las entradas del menú
    private int leerEnteroValido(Scanner scanner, int min, int max) {
        int valor;
        while (true) {
            if (scanner.hasNextInt()) {
                valor = scanner.nextInt();
                if (valor >= min && valor <= max) {
                    return valor;
                }
            } else {
                scanner.next();
            }
            System.out.print("Entrada inválida. Ingrese un número entre " + min + " y " + max + ": ");
        }
    }

    // Método para mostrar la tabla formateada
    public void mostrarTabla() {
        System.out.println("\n-------------------- TABLA DE VENTAS --------------------");
        System.out.printf("%-12s %-12s %-12s %-12s\n", "Mes", "Ropa (0)", "Deportes (1)", "Juguetería (2)");
        for (int i = 0; i < 12; i++) {
            System.out.printf("%-12s $%-11.2f $%-11.2f $%-11.2f\n",
                    meses[i], ventas[i][0], ventas[i][1], ventas[i][2]);
        }
        System.out.println("----------------------------------------------------------\n");
    }

    // Menú Interactivo
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Instanciación con la clase EjerArreglos
        EjerArreglos tienda = new EjerArreglos();
        int opcion = 0;

        do {
            System.out.println("===== MENÚ DE GESTIÓN DE VENTAS =====");
            System.out.println("1. Mostrar tabla completa de ventas");
            System.out.println("2. Insertar / Modificar venta");
            System.out.println("3. Buscar venta");
            System.out.println("4. Eliminar venta");
            System.out.println("5. Salir");
            System.out.print("Elija una opción: ");

            if (scanner.hasNextInt()) {
                opcion = scanner.nextInt();
                switch (opcion) {
                    case 1:
                        tienda.mostrarTabla();
                        break;
                    case 2:
                        tienda.insertarVentaConScanner(scanner);
                        break;
                    case 3:
                        tienda.buscarVentaConScanner(scanner);
                        break;
                    case 4:
                        tienda.eliminarVentaConScanner(scanner);
                        break;
                    case 5:
                        System.out.println("Saliendo del programa...");
                        break;
                    default:
                        System.out.println("Opción inválida.\n");
                }
            } else {
                System.out.println("Por favor, ingrese un número válido.\n");
                scanner.next();
            }

        } while (opcion != 5);

        scanner.close();
    }
}