#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main (void)
{

// ask for the name
   string s = get_string();
   printf("%c", toupper(s[0]));
   
   if (s != NULL)
   {

// with errors but mine
for (int i = 0, n = strlen(s); i < n; i++)
{
       while (s[i] != ' ' && s[i] != '\0')
       {
           i++;
       }
       printf("%c", toupper(s[i+1]));
}      
   
   printf("\n");
   return 0;
}}

/* no errors
if (isspace(s[i]) && !isspace(s[i+1]))
       {
           
       printf("%c", toupper(s[i+1]));
           
       }
       */