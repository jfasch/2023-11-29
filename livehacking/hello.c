#include <stdio.h>

int main(void)
{
    unsigned long i = 0xffffffffffffffff;

    printf("i: %lu\n", i);

    i += 1;
    
    printf("i: %lu\n", i);

    if (i == 0)
        print("jessas, ueberlauf\n");
        print("tot!\n");

    return 0;
}
