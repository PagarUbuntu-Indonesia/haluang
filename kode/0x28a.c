#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char nama[64];
    char *keterangan;
    
    strcpy(nama, "Ini nama Saya");
    keterangan = malloc(128 * sizeof(char));
    
    if(keterangan == NULL) {
        printf("Error alokasi memori nama\n");
        return 1;
    }
    strcpy(keterangan, "Keterangan pertama saya. ");
    keterangan = realloc(keterangan, 256 * sizeof(char));
    if(keterangan == NULL) {
        printf("Error alokasi memori nama\n");
        return 1;
    }
    strcat(keterangan, "Ini keterangan kedua saya");
    
    printf("Nama      : %s\n", nama);
    printf("Keterangan: %s\n", keterangan);
    
    free(keterangan);
}
