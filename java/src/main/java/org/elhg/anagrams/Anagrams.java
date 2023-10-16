package org.elhg.anagrams;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Anagrams {
        public static void main(String[] args) {
            /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
            Scanner scanner = new Scanner(System.in);
            String str1 = scanner.nextLine();
            String str2 = scanner.nextLine();
            //anagram
            //margana

            Map<String, Integer> frecuencyStr1 = frecuencyAnagram (str1.toLowerCase());
            Map<String, Integer> frecuencyStr2 = frecuencyAnagram (str2.toLowerCase());

            if(frecuencyStr1.equals(frecuencyStr2)){
                System.out.println("Anagrams");
            }else{
                System.out.println("Not Anagrams");
            }

        }

        private static Map<String, Integer> frecuencyAnagram (String str){
            Map<String, Integer> frecuencyStr = new HashMap<>();
            for (int i=0 ; i<str.toCharArray().length; i++){
                char c = str.toCharArray()[i];
                String key = (str.toCharArray()[i]+"");
                if(frecuencyStr.containsKey(key)){
                    int freq = frecuencyStr.get(key);
                    freq++;
                    frecuencyStr.put(key,freq);
                }else{
                    frecuencyStr.put(key,1);
                }
            }
            return frecuencyStr;
        }
}
