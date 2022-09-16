fn soma(x : i32, y : i32) -> i32{

  var x : i32;
  x = y + y;
  Print(x);
  return(x);
}

void main() {
  var a : i32;
  var b : i32;
  a = 3;
  b = soma(a, 4)+1;
  Print(a);
  Print(b);
}