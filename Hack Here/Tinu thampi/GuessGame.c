#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
    int number,guess,nguess=1;
    srand(time(0));
    number=rand()%100 + 1;
    
    do{
        printf("Enter a number between 1 to 100\n");
        scanf("%d", &guess);

        if(number>guess){
            printf("Guess something Higher!!\n");
        }

        else if(number<guess){
            printf("Guess something lower\n");
        }

        else{
            printf("You guessed it right!! the number of guesses taken %d\n", nguess);
    }
        nguess++;
    }
    while (guess!=number);
   
    return 0;
}