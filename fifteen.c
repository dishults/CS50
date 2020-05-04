/**
 * fifteen.c
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man usleep` for more.
 */
 
#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);

int main(int argc, string argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }


    // ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }

    // open log
    FILE *file = fopen("log.txt", "w");
    if (file == NULL)
    {
        return 3;
    }

    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while (true)
    {
        // clear the screen
        clear();

        // draw the current state of the board
        draw(); 

        // log the current state of the board (for testing)
        for (int i = 0; i < d; i++)
        {
            for (int j = 0; j < d; j++)
            {
                fprintf(file, "%i", board[i][j]);
                if (j < d - 1)
                {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);

        // check for win
        if (won())
        {
            printf("ftw!\n");
            break;
        }

        // prompt for move
        printf("Tile to move: ");
        int tile = get_int();
        
        // quit if user inputs 0 (for testing)
        if (tile == 0)
        {
            break;
        }

        // log move (for testing)
        fprintf(file, "%i\n", tile);
        fflush(file);

        // move if possible, else report illegality
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }

        // sleep thread for animation's sake
        usleep(500000);
    }
    
    // close log
    fclose(file);

    // success
    return 0;
}

/**
 * Clears screen using ANSI escape sequences.
 */
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

/**
 * Greets player.
 */
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF FIFTEEN\n");
    usleep(2000000);
}

/**
 * Initializes the game's board with tiles numbered 1 through d*d - 1
 * (i.e., fills 2D array with values but does not actually print them).  
 */
void init(void)
{
    int desk = d*d;
if (d%2 == 1) // check if d is odd or even number
{
    for (int i = 0; i < d; i++) // for each row
    {
        for (int j = 0; j < d; j++) // for each column
        {
            desk -= 1;
            board[i][j] = desk; // SET VALUE FOR TILE
        }
    }
}
else
{
    for (int i = 0; i < d; i++) // for each row
    {
        for (int j = 0; j < d; j++) // for each column
        {
            // swap 1 and 2 if d is even number
            if (i == d-1 && j == d-3)
            {
                desk -= 1;
                board[i][j] = 1;
            }
            else if (i == d-1 && j == d-2)
            {
                desk -= 1;
                board[i][j] = 2;
            }
            else
            {
                desk -= 1;
                board[i][j] = desk; // SET VALUE FOR TILE
            }
        }
    }
}
}
/**
 * Prints the board in its current state.
 */
void draw(void)

{
   for (int i = 0; i < d; i++) // for each row
    {
        for (int j = 0; j < d; j++) // for each column
        {
                if (board[i][j] == 0) // 0 is _
                {
                    printf("%3s", "_"); // take out '3' for check50
                }
                else
                {
                    printf("%3i", board[i][j]); // PRINT TILE's VALUES
                }
        }
        printf("\n"); // print new line
        
    }
    
}

/**
 * If tile borders empty space, moves tile and returns true, else
 * returns false. 
 */
bool move(int tile) 
{
for (int z = 0; z < d; z++) // for each row
{
    for (int x = 0; x < d; x++) // for each column
    {
        if (board[z][x] == 0)
        {
            // checks if the move is possible
            if (tile == board[z+1][x] || tile == board[z-1][x] || tile == board[z][x+1] || tile == board[z][x-1])
            {
                // SWITCH TILE WITH _
                for (int i = 0; i < d; i++) // for each row
                {
                    for (int j = 0; j < d; j++) // for each column
                    {
                        if (board[i][j] == tile)
                        {
                            board[i][j] = 0;          
                        }
                        else if (board[i][j] == 0)
                        {
                            board[i][j] = tile;          
                        }
                    }
                }
                
                return true; 
            }
            else
            {
                return false;
            }
        }
    }
}
return false;
}

/**
 * Returns true if game is won (i.e., board is in winning configuration), 
 * else false.
 */
bool won(void)
{
    for (int i = 0; i < d; i++) // for each row
    {
        for (int j = 0; j < d;) // for each column
        {
            if (board[i][j] < board[i][j+1] || board[i][j] < board[i+1][j-(d-1)])
            {
                j++;
            }
            else if (board[i][j] == board[d-1][d-2])
            {
                if (board[d][d] == 0)
                {
                    j++;
                    return true;
                }
            }
            else
            {
               return false; 
            }
        }
    }
    return true;
}
