// Solicitar una lista de numeros enteros al usuario
// Sumar cada elemento de la lista e imprimir

import 'dart:io';

void main() {
  List <int> Lista_1 = [];

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
      Lista_1.add(elemento);
    }
  }
  print("La lista ingresada es: $Lista_1");
  int listaSuma = Lista_1.reduce((a, b) => a+b);
  print("La suma de la lista resultante es: $listaSuma");
  }
