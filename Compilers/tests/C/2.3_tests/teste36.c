int soma(int x) {

  if (x < 3) {
    printf(x);
    soma(x+1);
  }
}

void main() {
  soma(1);
}