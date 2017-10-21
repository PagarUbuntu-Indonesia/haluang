#include <stdio.h>
#define BULAN 12

int main()
{
  int hari[BULAN] = {31,28,31,30,31,30, 31,31,30,31,30,31};
  int index;

  for(index=0; index<BULAN; index++)
    printf("Bulan %2d ada %d hari\n", index+1, hari[index]);
}
