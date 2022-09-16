fn soma(x : i32) {

  if (x < 3) {
    Print(x);
    soma(x+1);
  }
}

fn main() {
  soma(1);
}