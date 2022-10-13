#include <stdio.h>
#include <stdlib.h> 
int main( )
{
    // Declare pointer variables
    int  *i ;
    float  *a ; 
    /* Allocate memory using malloc and store the starting 
    address of allocated memory in pointer variable*/
    i = (int*) malloc (sizeof(int));
    a = (float*) malloc (sizeof(float));
    // Declare employee structure
    struct emp
    {
        char name [20];
        int age;
        float sal;
    };
    // Declare structure pointer
    struct emp *e;
    e = (struct emp *) malloc (sizeof (struct emp));
}
