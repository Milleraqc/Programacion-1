import java.util.Scanner;

public class Parcial2 {
    public static void main(String[] args) {
        Scanner consola = new Scanner(System.in);
        
        System.out.println("Dijite un numero");
        int numero = consola.nextInt();
        
        if (numero < 10){
            System.out.println("Numero : " + numero);
        }else{
            int suma = 0;
            
            while (numero > 0){
                suma += numero%10;
                numero /= 10;
            }
            System.out.println("La suma de las cifras del numero digitado : " + suma);
        }
    }
}