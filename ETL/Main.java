import java.util.*;
import java.io.*;
import java.lang.*; 

public class Main {

    static double kmtokm(double km){ //     km/h ke km/h
        return km * 1.0; }

    static double mstokm(double ms){ //    m/s ke km/h
        return ms * 3.6; }

    static double miltokm(double mil){ //   mil/h  ke km/h
        return mil * 1.60934; }

    static double knottokm(double knot){ //   knot  ke km/h
        return knot * 1.852; }    

  public static void main(String[] args) {
 
    // double km = 10;
    // double ms = 2.5;
    // double mil = 25;
    // double knot = 12;

      // System.out.println(km + " km/jam = " + kmtokm(km) + " km/jam");
      // System.out.println(ms + " m/s to = " + mstokm(ms) + " km/jam");
      // System.out.println(mil + " mil/jam = " + miltokm(mil) + " km/jam");
      // System.out.println(knot + " knot = " + knottokm(knot) + " km/jam");
    
    System.out.println("Inputan: ");
    Scanner input = new Scanner(System.in);  
    String inputan = input.nextLine();

    String angka = inputan.replaceAll("[^0-9.]+", " ");        
    double valHitung = Double.parseDouble(angka);

    if(inputan.contains("km/jam")){
        System.out.println(valHitung + " km/jam = " + kmtokm(valHitung) + " km/jam");

    } else if(inputan.contains("m/s")){
        System.out.println(valHitung + " m/s = " + mstokm(valHitung) + " km/jam");

    } else if(inputan.contains("mil/jam")){
        System.out.println(valHitung + " mil/jam = " + miltokm(valHitung) + " km/jam");

    } else if(inputan.contains("knot")){
        System.out.println(valHitung + " knot = " + knottokm(valHitung) + " km/jam");

    } else
        System.out.println("format belum sesuai");
    
  }
}