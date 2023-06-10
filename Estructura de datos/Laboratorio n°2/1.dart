// Crear dos listas
// La segunda debe contener 10 elementos, generados de forma aleatoria
// entre -1 a -5
// Se suman ambas listas y se imprime la resultante
// Luego se remueve el 7mo y 8vo elemento de la lista anterior
import 'dart:math';
void main() {
  List lista_1 = [3,4,7,9,8,5,1,2,5,7];
  Random random = Random();
  List lista_2 = List.generate(10, (index) => -random.nextInt(5) - 1);

  print("La lista 1 es: $lista_1");
  print("La lista 2 es: $lista_2");
//Completado luego de laboratorio:
  List lista_suma = [];
  for (int i = 0; i < 10 ; ++i){
  lista_suma.add(lista_2[i] + lista_1 [i]);
    }
  print("La lista resultante es: $lista_suma");
  lista_suma.removeRange(6,8);
  print ("La lista removiendo elementos es: $lista_suma");
  }

