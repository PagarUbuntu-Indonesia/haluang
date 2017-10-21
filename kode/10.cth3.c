#include <stdio.h>
#define NAMA    "Haluang"
#define WEB     "Haluang.com"
#define PENULIS "Jockerz"
#define INFO    "Tutorial pemograman dasar"

void tentang()
{
  printf("Nama ~\t%s\n",NAMA);
  printf("Web: ~\t%s\n",WEB);
  printf("Penulis ~ %s\n",PENULIS);
  printf("Info ~\t%s\n",INFO);
}
void cetak_garis() {
  int i;

  for(i=0; i<48; i++) printf("*");
  printf("\n");
}

int main()
{
  cetak_garis();
  tentang();
  cetak_garis();
}
