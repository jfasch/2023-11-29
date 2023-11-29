#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* create_str()
{
    return malloc(3);
}


int main(void)
{
    int i;
    for (i = 0; i<100000; i++) {
        char* str = create_str();
        strcpy(str, "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj");
        printf("%s\n", str);
    }
    return 0;
}
