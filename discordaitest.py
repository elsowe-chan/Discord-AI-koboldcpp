import discord
import requests
import chathistory
from chathistory import add_new_entry
from chathistory import write_to_file

intents = discord.Intents.all()
client = discord.Client(intents=intents)
txt_file_content = "test.txt"
txt_history_content = "chat_history.txt"

#replace ("AI: "; "") by what you want to delete before sending it to discord
def format_response(text):
    text = text.replace("AI: ", "")
    return text.replace("user: ", "")

@client.event
async def on_message(message):
    global user_id, user_message, user_username
    user_id = str(message.author.id)
    user_username = message.author.display_name
    user_message = message.content
    usercontent = user_username + " : " + user_message
    excluded_ids = {"0000000", "0000000", "000000000"}
    #add bot/user id that you don't want to interract with the AIbot
    if user_id in excluded_ids: 
        return

    with open(txt_file_content, 'r') as f:
        txt_content = f.read()
    
    with open(txt_history_content, 'r') as f:
        txt_history = f.read()
    #replace "127.0.0.1:5001" with your ip and port
    url = "http://127.0.0.1:5001/v1/chat/completions"
    payload = {
        "messages": [
            {
                "role": "system",
                "content": txt_content + txt_history,
            },
            {
                "role": "user",
                "content": usercontent,
            }
        ],
        "max_tokens": 120, #change the maximum number of tokens used by the AIbot
        "stop": "\n"  #change what stop the bot generation (curently the bot stop generating when jumping a line)
    }
    headers = {}
    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()
    output = response_data["choices"][0]["message"]["content"]

    formatted_output = format_response(output)
    await message.channel.send(formatted_output)

    add_new_entry(usercontent, formatted_output)  # store a new conversation entry
    # write_to_file(txt_content, "chat_history.txt")  # save chat history to file
    print(output)
    print("completion token:", response_data["usage"]["completion_tokens"])
    print("total token:", response_data["usage"]["total_tokens"])
    print("prompt token:", response_data["usage"]["prompt_tokens"])

#add your bot token here
client.run('TOKEN')
