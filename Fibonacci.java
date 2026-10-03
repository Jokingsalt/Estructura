public class Fibonacci {

    public static void main(String[] args) {
        System.out.println("Forzando StackOverflowError...");
        calcularFibonacci(0);
    }

    public static long calcularFibonacci(long n) {
        // Al imprimir, verás hasta qué nivel de profundidad llegó la pila antes de
        // colapsar
        System.out.println("Nivel de profundidad en la pila: " + n);

        // Llamada recursiva directa: la función Nunca retorna,
        // por lo que cada llamada queda 'atrapada' reteniendo memoria en la pila.
        return calcularFibonacci(n + 1);
    }
}