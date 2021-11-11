# Google Hangouts Analytics 🔬

Run this code in the same folder as your groupchat formatted as a csv (see JSON -> CSV converter).
Make sure you have a way to run python code and have used pip to installed venv.

### Starting off
First, run the command

`$python3 -m venv ./env` to create a virtual environment in which to store your dependencies. 

Next, run `$source env/bin/activate` in the project directory to start your venv. Once you are in a venv, you can install all dependencies for this project by running `$python3 -m pip install -r requirements.txt`

## Don't have a file for you groupchat ?
>Go to Takeout.Google.com to request a zip file of your Hangouts data
>place groupchat in the same directory as the .py code from this project

### Once you download the code, you have the option to:

* see all previous chat names of the groupchat

* see how many messages a person has sent

* see how many words a person has sent

* see how many words a person sends per message on average

* filter the data to exclude empty messages and hyperlinked messages

* generate a cool word cloud of the most frequent (uncommon) words used in the chat

