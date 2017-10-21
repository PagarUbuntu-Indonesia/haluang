/* 0x05-bitwise.c */
#include <stdio.h>

int main()
{
    int var1 = 5;
    int var2 = 7;
    int oper;

    oper = var1 & var2;
    printf("var1 AND var2\t= %d\n",oper);

    oper = var1 | var2;
    printf("var1 OR var2\t= %d\n",oper);

    oper = var1 ^ var2;
    printf("var1 EX-OR var2\t= %d\n",oper);

    oper = ~var2;
    printf("~var2\t\t= %d\n",oper);

    return 0;
}