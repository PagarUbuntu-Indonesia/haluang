#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char *ptr; // pointer ke
    ptr = malloc(39 * sizeof(char));
    
    if(ptr == NULL) {
        printf("Error: gagal mengalokasikan memori\n");
        return 1;
    }
    
    strcpy(ptr, "Konten untuk ptr");
    printf("ptr   : %s\n", ptr);
    free(ptr);

    return 0;
}
