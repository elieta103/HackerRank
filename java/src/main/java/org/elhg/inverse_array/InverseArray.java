package org.elhg.inverse_array;

import java.util.ArrayList;
import java.util.List;

public class InverseArray {
    public static void main(String[] args) {
        List<Integer> listOriginal = List.of(1,2,3);
        List<Integer> listModif = reverseArray(listOriginal);
        System.out.println(listModif);
    }

    public static List<Integer> reverseArray(List<Integer> a) {
        List<Integer> listModif = new ArrayList<>();
        for(int i = a.size()-1; i>=0; i--){
            listModif.add(a.get(i));
        }
        return listModif;
    }
}
