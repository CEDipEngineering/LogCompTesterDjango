fn soma(x : i32) -> i32 {

  if (x < 3) {
    Print(x);
    x = soma(x+1);
  }
  return(x);  
}

fn main() {
  var x : i32;
  x = soma(1);
}