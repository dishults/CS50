#include <stdio.h>
#include <cs50.h>

int main (void)
{
int height = 0;


do                          // do-while loop to continue asking for a valid input
   {
    printf("Height: ");
    height = get_int();
   }
while (height < 0 || height > 23);

for (int i = 0; i < height; i++)  // rows
{
    for (int j = 0; j < height-i-1; j++)  // spaces
    {
        printf("%s", " ");
    } 

 for (int k = 0; k < i+2; k++)  // hashes
    {
        printf("#");
    }
    
printf("\n");
}

}

