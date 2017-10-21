#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    int  *nilai;
    char *nama;
};

typedef struct LinkedList {
    struct Node node;
    struct Node *link_kiri;
    struct Node *link_kanan;
};

int main()
{
    struct LinkedList ptr0, ptr1, ptr2;

    ptr0 .node->nilai = malloc(sizeof(int));
    ptr0 .node->nama  = malloc(16 * sizeof(char));
    ptr1 .node->nilai = malloc(sizeof(int));
    ptr1 .node->nama  = malloc(16 * sizeof(char));
    ptr2 .node->nilai = malloc(sizeof(int));
    ptr2 .node->nama  = malloc(16 * sizeof(char));

    ptr0 -> link_kiri  = &ptr1;
    ptr0 -> link_kanan = &ptr2;
 
    ptr0 -> node -> nilai = 0;
    strcpy(ptr0 -> node -> nama, "Node root");
    ptr1 -> node -> nilai = -1;
    strcpy(ptr1 -> node -> nama, "Node kiri");
    ptr0 -> node -> nilai = 1;
    strcpy(ptr2 -> node -> nama, "Node kanan");
    
    printf("Nama: %s - nilai: %d\n", ptr0->nama, ptr0->nilai);
    printf("Nama: %s - nilai: %d\n", \
        ptr0-> link_kiri-> nama, \
        ptr0-> link_kiri-> nilai); 
    printf("Nama: %s - nilai: %d\n", \
        ptr0-> link_kanan-> nama, \
        ptr0-> link_kanan-> nilai); 
}
