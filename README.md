# Discord AI Koboldcpp

Discord AI Koboldcpp is a simple puthon script that catch a discord message and then send it to Koboldcpp API to generate a respond and then send the respond back to the discord channel where the messagec come from.

# test.txt
this file is where you write the guideline of your AIBOT.
\
for exemple :\
"you are an AI bot."
\
"assist user and respond to them."

# chat_history.txt
this file containt the history of users and AI message.
\
the content of this file is resend to the AI everytime a new message need to be generated so the AI is able to know what was previously said.
\
for exemple :\
"this is the current history of chat. 
NEVER use "User:".
Chat history :

User: Elsowe chan : respond with a fun welcome quote say by HALL 9000 in the movie 2001 a space odyssey
AI(you): Hall 9000: "Greetings, Chan. I am pleased to make your acquaintance. How may I be of service to you today?"
"\

in this exemple the AI cuted my username in half and only used "chan" instead of "Elsowe-chan".

![Screenshot](https://imgur.com/hPbnEVs.png)

# discordaitest.py
this file containt the main script.\
in this file you will need to change or custom this value : \

```
def format_response(text):\
    text = text.replace("AI: ", "")\
    return text.replace("user: ", "")
```

this code delete "AI: " and "user: " from the discord reply of the bot.\
in the previous screenshot i didn't writed "Hall 900: " this is why it was in the message of the bot.
```
 excluded_ids = {"0000000", "0000000", "000000000"}
```
replace the 0 by the user or bot id that will have her message ignored by the AI.

```
    url = "http://127.0.0.1:5001/v1/chat/completions"
```
replace "127.0.0.1:5001" with your ip and port of your Koboldcpp endpoint.

```
client.run('TOKEN')
```
replace TOKEN by your discordbot TOKEN

# chathistory.py
the script that add the message of the user and bot to the chat_history.txt file
