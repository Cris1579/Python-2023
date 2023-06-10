import 'dart:math';

void main() {
  Random random = Random();
  var Lista_1= List.generate(10, (index) =>random.nextInt(5) + 1);
  print (Lista_1);
  //var Lista_1= List.generate(10, (index) =>random.nextInt(-5) + 1)
  //El random.nextInt trabaja solo con positivos
}