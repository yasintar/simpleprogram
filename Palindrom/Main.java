import java.util.Stack;
import java.util.Scanner;

public class Main {
  static void cekPalindrom() {
        System.out.println("Inputan:");
        Scanner input = new Scanner(System.in);
        String inputan = input.nextLine();
        
        Stack stack = new Stack();
        String rvinput = "";

        for (int i = 0; i < inputan.length(); i++) {
            stack.push(inputan.charAt(i));
        }

        while (!stack.isEmpty()) {
            rvinput = rvinput + stack.pop();
        }

        if (inputan.equals(rvinput))
            System.out.println("Ya," + "'" + inputan + "'" + " adalah palindrom");
        else
            System.out.println("Tidak, karena " + "'" + rvinput + "'" + " tidak sama dengan " + inputan);
  }

  public static void main(String[] args) {
    cekPalindrom();
  }
}