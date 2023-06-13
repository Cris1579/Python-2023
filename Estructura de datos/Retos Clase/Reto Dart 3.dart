// Crear una lista de n° enteros donde se ingrese el tamaño
// y los elementos por teclado.
// Se debe ordenar ascendemente y descendentemente.
// Solo se deben n° enteros positivos
// Además, encontrar valor máximo y mínimo de la lista.
import 'dart:io';
void main() {
  List<int> lista_enteros = [];

  stdout.write("Ingrese el tamaño de la lista: ");
  int size = int.parse(stdin.readLineSync()!);
  if (size < 0) {
    print("No se admiten n° negativos");
  } else {
    ;
    stdout.write("Ingrese los elementos de su lista: ");
    for (int i = 0; i < size; i++) {
      stdout.write('\n Elemento ${i + 1}: ');
      int elemento = int.parse(stdin.readLineSync()!);
      lista_enteros.add(elemento);
    }
    print("La lista ingresada es: $lista_enteros");
    lista_enteros.sort();
    print("La lista ordenada ascendentemente es: $lista_enteros");

    lista_enteros.sort((a, b) => b.compareTo(a));
    print("La lista ordenada descendentemente es: $lista_enteros");

    int max = lista_enteros.reduce((a, b) => a > b ? a : b);
    print("El valor máximo de la lista es: $max");

    int min = lista_enteros.reduce((a, b) => a < b ? a : b);
    print("El valor minimo de la lista es: $min");
  }
}