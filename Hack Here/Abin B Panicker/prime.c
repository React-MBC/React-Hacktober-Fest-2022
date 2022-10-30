#include <stdio.h>

int main() {

  int n, i, flag = 0;
  printf("Enter an integer to check prime: ");
  scanf("%d", &n);

 
  if (n == 0 || n == 1)
    flag = 1;

  for (i = 2; i <= n / 2; ++i) {

   
    if (n % i == 0) {
      flag = 1;
      break;
    }
  }

  // flag is 0 for prime numbers
  if (flag == 0)
    printf("The given number is a prime number.", n);
  else
    printf("The given number  is not a prime number.", n);

  return 0;
}
