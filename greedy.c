#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main (void)
{
float input = 0.00;

do                          
   {
    printf("O hai! How much change is owed?\n");
    input = get_float();
    }
while (input < 0);



int cents = round(input * 100);
int n = 0;


while (cents >= 25)
{
    n++;
    cents = cents - 25;
}

while (cents >= 10)
{
    n++;
    cents = cents - 10;
}

while (cents >= 5)
{
    n++;
    cents = cents - 5;
}

while (cents > 0)
{
    n++;
    cents = cents - 1;
}


printf("%i\n", n);
}