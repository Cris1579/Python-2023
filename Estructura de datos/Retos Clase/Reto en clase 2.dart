// Crear un arreglo de tamaño aleatorio (entre 10 a 30 elementos).
// Los elementos también deben ser aleatorios (de 0 a 10),
// Además se solicita ordenarlo de forma ascendente
// Luego ordenarlo de forma aleatoria
// En dart

import 'dart:math';

void main() {
  Random random = Random();
  var tamanoLista = random.nextInt(21) + 10; //random.nextInt saca un número entre el que indique
  var lista = List.generate(tamanoLista, (index) => random.nextInt(11));

  print('El tamaño de la lista es: $tamanoLista');
  print('La lista es: $lista');
  lista.sort();
  print("La lista ordenada de forma ascendete queda: $lista");
  lista.shuffle();
  print('La lista ordenada de forma aleatoria queda: $lista');
}
