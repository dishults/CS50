# Project 3: Pizza

Web application for handling a pizza restaurant’s online orders with:
- **Menu**: web application supports all of the available menu items for [Pinnochio’s Pizza & Subs](http://www.pinocchiospizza.net/menu.html) (a popular pizza place in Cambridge).
- **Adding Items**: Using Django Admin, site administrators (restaurant owners) are able to add, update, and remove items on the menu.
- **Registration, Login, Logout**: Site users (customers) are able to register for the web application with a username, password, first name, last name, and email address. Customers are then able to log in and log out of the website.
- **Shopping Cart**: Once logged in, users can see a representation of the restaurant’s menu, where they can add items (along with toppings or extras, if appropriate) to their virtual “shopping cart.” The contents of the shopping is saved even if a user closes the window, or logs out and logs back in again.
- **Placing an Order**: Users are able to place an order at the Checkout, whereby the user is asked to confirm the items in the shopping cart, and the total before placing an order.
- **Viewing Orders**: Site administrators have access to a page where they can view any orders that have already been placed.
- **Personal Touch**: Allowing site administrators to mark orders as Recieved/Prepaired/Withdrawn and allowing users to see the status of their pending or completed orders.

>What is a “Special” pizza? In this implimentation, it allows for 5 different types of toppings.