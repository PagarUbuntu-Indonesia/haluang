#include <stdio.h>

union Union {
    int    i;
    float  f;
    char   str[10];
    double d;
};

int main() {
    union Union u;
    
    printf("Ukuran memori union \"u\": %d\n", sizeof(u));
    
    return 0;
}
