#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

//get key from command line argument
int main (int argc, string argv[])
{
if (argc < 2 || argc > 2)
{
    printf("Usage: ./caesar k\n");
    return 1;
}


else
//for each character in the plaintext string
    {
       
    int k = atoi(argv[1]);      //turn key into integer
    

    printf("plaintext: ");      //prompt for plaintext
    string p = get_string();

printf("ciphertext: ");
for (int i = 0, n = strlen(p); i < n; i++)
    
    if (isspace(p[i]))
    {
        printf(" ");
    }
    //else if puctiation
    else if (ispunct(p[i]))
    {
        if (p[i] == ',')
        {
            printf(",");
        }
        else if (p[i] == '!')
        {
            printf("!");
        }
        else if (p[i] == '?')
        {
            printf("?");
        }
        else
        {
            printf(".");
        }
    }
    
    //if alphabetic
    else if (isalpha(p[i]))
    {

        //preserve case
        if (isupper(p[i]))
        {
            p[i] -= 65; // ASCII to alphabetical (CAPS)
            
            //shift plaintext by key and print
            printf("%c", toupper(((p[i] + k)%26) + 65));
        }
        
        else
        {
            p[i] -= 97; // // ASCII to alphabetical (lows)
            
            printf("%c", tolower(((p[i] + k)%26) + 97));
        }

    }
    }
printf("\n");

    return 0;
}