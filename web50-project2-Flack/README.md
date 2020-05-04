# Project 2: Flack

Online messaging service using Flask, similar in spirit to Slack with:
- **Display Name**: When a user visits web application for the first time, they are prompted to type in a display name that will eventually be associated with every message the user sends. If a user closes the page and returns to the app later, the display name is still remembered.
- **Channel Creation**: Any user is able to create a new channel, so long as its name doesn’t conflict with the name of an existing channel.
- **Channel List**: Users are able to see a list of all current channels, and selecting one allows the user to view the channel.
- **Messages View**: Once a channel is selected, the user can see any messages that have already been sent in that channel, up to a maximum of 100 messages. The app only stores the 100 most recent messages per channel in server-side memory.
- **Sending Messages**: Once in a channel, users are able to send text messages to others in the channel. When a user sends a message, their display name and the timestamp of the message are associated with the message. All users in the channel can then see the new message (with display name and timestamp) appear on their channel page. Sending and receiving messages does not require reloading the page.
- **Remembering the Channel**: If a user is on a channel page, closes the web browser window, and goes back to your the application, the application remembers what channel the user was on previously and takes the user back to that channel.
- **Personal Touch**: Additional feature is when a user sends a messages that starts with @ it converts and sends:
    - `@time`: current time
    - `@date`: current date
    - `@len`: number of messages in the channel
    - `@me`: your username
    - `@channels` : all available channels
