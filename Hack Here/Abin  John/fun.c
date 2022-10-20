# include <stdio.h>
void dbl ( int * ) ;
void tple ( int * ) ;
void qdpl ( int * ) ;
int main( )
{
    int  num = 2, i ;
    void ( *p[ ] )( int * ) = { dbl, tple, qdpl } ;
    for ( i = 0 ; i < 3 ; i++ )
    {
        p[ i ]( &num ) ;
        printf ( "%d\n", num ) ;
    }
    return 0 ;
}
 
void dbl ( int *n )  
{
    *n = *n * *n ;
}
 
void tple ( int *n )  
{
    *n = *n * *n * *n ;
}
 
void qdpl ( int *n )  
{
    *n = *n * *n * *n * *n ;
}