# Google Hangouts Analytics

Run this code in the same folder as a groupchat csv.
Make sure you have a way to run python code.

Don't have one?
>Go to Takeout.Google.com to request a zip file of your Hangouts data
>place groupchat in the same directory as the .py code from this project

This code has functions that can:

tell you all previous chat names of the groupchat

tell you how many messages a person has sent

tell you how many words a person has sent

tell you how many words a person sends per message on average

filter the csv to exclude empty messages and hyperlinked messages

generate a cool word cloud of the most frequent (uncommon) words used in the chat

## To Do
* add some argparsing to make this useful in command line (Unix)
* Try to add more graphical representations of the data built in (-g option?)
* Make it more clear as an API, right now the file itself needs to be written to customize output 
