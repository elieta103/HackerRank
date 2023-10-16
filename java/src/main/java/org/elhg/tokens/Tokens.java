package org.elhg.tokens;

import java.util.Scanner;

public class Tokens {
    public static void main(String[] args) {
        Scanner scan = scan.nextLine();
        String s = scan.nextLine();
        scan.close();
        if (s.trim().isEmpty()) {
            System.out.println(0);
        }
        else{
            /*
            * ^ Inicio de una cadena o multilinea
            * \ Escape \
            * \W Not Word, matches any caracter, thats in not word carcter
            * + Mas de un carater
            * ***************************************************************
            * []  Conjunto de caracteres
            * \ Escape \
            * \s Espacio en blanco
            * !,?._'@  Match Caracteres
            * */

            String[] splitString = (s.replaceAll("^\\W+", "").split("[\\s!,?._'@]+"));
            System.out.println(splitString.length);
            for (String string : splitString) {
                System.out.println(string);
            }
        }
    }
}
