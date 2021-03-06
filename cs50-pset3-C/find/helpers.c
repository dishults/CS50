/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>
#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)         // (needle, haystack, size)
{
    // TODO: implement a searching algorithm
    int end = n-1;
    int start = 0;
    

    while (end >= start)
    {
        int mid = (start + end)/2;
        if (values[mid] == value)
        {
            return true;
        }
        
        else if (values[mid] > value)
        {
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
        
    }
       
    return false;
        
}


/**
 * Sorts array of n values.
 */
void sort(int values[], int n)      // (haystack, size)
{
    int temp;
    int j = n;

    // TODO: implement a sorting algorithm
    while (j != 1)
    {
    for (int i = 0; i < j-1; i++, j--)
    {
        if (values[i] > values[i+1])
        {
            temp = values[i];
            values[i] = values[i+1];
            values[i+1] = temp;
        }
        
    }}
    
    return;
}
