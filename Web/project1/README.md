# Project 1

Book review website with:
- **Registration**: Users are able to register, providing a username and password.
- **Login**: Users, once registered, are able to log in with their username and password.
- **Logout**: Logged in users are able to log out of the site.
- **Import**: Python program to import books from CSV file to PostgreSQL database.
- **Search**: Once a user has logged in, they are taken to a page where they can search for a book. Users are able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, the website displays a list of possible matching results, or a message if there were no matches. If the user typed in only part of a title, ISBN, or author name, search page still finds matches for those as well!
- **Book Page**: When users click on a book from the results of the search page, they are taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on the website.
- **Review Submission**: On the book page, users are able to submit a review: consisting of a rating on a scale of 1 to 5, as well as an opinion about a book. Users are not able to submit multiple reviews for the same book.
- **Goodreads Review Data**: On the book page, it is also displayed (if available) the average rating and number of ratings the work has received from Goodreads.
- **API Access**: If users make a GET request to the website’s `/api/<isbn>` route, where `<isbn>` is an ISBN number, the website returns a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. The resulting JSON follows the format:
```
{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
}
```