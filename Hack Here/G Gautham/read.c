#include <stdio.h>
int main() {
 FILE *fp;
 char ch;
 /*Open file in read mode*/
 fp= fopen ('example.txt', 'r');
 while( (ch = getc(fp)) != EOF) {
  /*getc() function reads a character and its value is stored in variable 'ch' until EOF is encountered*/
  printf('%ch', ch);
 }
  fclose(fp);
  return 0;
}