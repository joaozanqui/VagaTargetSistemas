#include <stdio.h>

int main()
{
    int num, primeiro = 0, segundo = 1, prox, pertence = 0;
    int i;

    printf("Digite o numero: ");
    scanf("%d", &num);

    for (i = 0; i <= num; i++)
    {
        if (i <= 1)
            prox = i;
        else
        {
            prox = primeiro + segundo;
            primeiro = segundo;
            segundo = prox;
        }

        if(prox==num)
        {
            pertence = 1;
            break;
        }
    }

    if(pertence==1)
        printf("%d pertence a sequencia de Fibonacci", num);
    else
        printf("%d nao pertence a sequencia de Fibonacci", num);

    return 0;
}
