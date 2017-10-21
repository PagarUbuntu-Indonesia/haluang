#include <stdio.h>

int main()
{
    int A=4, B=7;
    printf("sizeof(int): %d\n", sizeof(int));

    printf("A & B = %d\n", A&B);
    printf("A | B = %d\n", A|B);
    printf("A ^ B = %d\n", A^B);
    printf("  ~ B = %d\n",  ~B);
    printf("A << 2= %d\n", A<<2);
    printf("A >> 2= %d\n", A>>2);
}
