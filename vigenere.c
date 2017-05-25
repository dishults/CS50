#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

//get key from command line argument
int main (int argc, string argv[])
{
if (argc == 2)
{
    
    
    string k = argv[1];      //turn key into string
    int m = strlen(k);
    
    for (int c = 0; c < m;)     //check if every char in argv is alphabetical
    {
       if (isalpha(k[c]))
       {
           c++;
       }
       else
       {
           printf("error\n");
           return 1;
       }
    }

    printf("plaintext: ");      //prompt for plaintext
    string p = get_string();

int j = 0;                      //for key count
printf("ciphertext: ");

for (int i = 0, n = strlen(p); i < n; i++)
 {
   
    //if alphabetic
    if (isalpha(p[i]) && isalpha(k[j]))
    {
        //preserve case
        
        if (islower(p[i]) && islower(k[j]))    // all lows
        {
            printf("%c", tolower(((p[i]-97) + (k[j]-97))%26)+97);       //shift plaintext by key and print
            
            j = (j + 1)%m;                      //make sure the key repeats after it reaches the last letter
        }    
        
        else if (isupper(p[i]) && isupper(k[j])) // all CAPS
        {
            printf("%c", toupper(((p[i]-65) + (k[j]-65))%26)+65);
            j = (j + 1)%m; 
        }
        
        else if (isupper(p[i]) && islower(k[j])) // P and k
        {
            printf("%c", toupper(((p[i]-65) + (k[j]-97))%26)+65);
            j = (j + 1)%m; 
        }
        
        else                                    // p and K
        {
            printf("%c", tolower(((p[i]-97) + (k[j]-65))%26)+97);
            j = (j + 1)%m; 
        }
        
        

    }
        //if space
    else if (isspace(p[i]))     
    {
        printf(" ");
    }
        //if puctiation
    else if (ispunct(p[i]))
    {
        printf ("%c", p[i]);
    }
    else
    {
        printf("missing condition");
    }
 }
    
}
else 
{
    printf("Usage: ./vigenere k\n");
    return 1;
}
printf("\n");
}