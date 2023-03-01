#include <stdio.h>
#include <string.h>

#define MAX 30

int main()
{
    int i, j;
    char string[MAX], invertida[MAX];

    printf("Escreva uma frase de ate %d caracteres: ", MAX);
    gets(string);

    int tamanho = strlen(string);
    j = tamanho - 1;

    for(i = tamanho; i<MAX; i++)
        invertida[i] = '\0';

    for(i=0; i<tamanho; i++, j--)
        invertida[j] = string[i];

    printf("%s\n", invertida);

    return 0;
}
