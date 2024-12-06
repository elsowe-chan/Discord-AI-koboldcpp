import os

def store_chat_history(txt_filename):
    def write_to_file(chat_history, filename):
        if os.path.isfile(filename):
            with open(filename, "a") as f:
                f.write(chat_history + "\n\n")
        else:
            with open("chat_history.txt", "a") as f:
                f.write(chat_history + new_chat_history + '\n\n')
                #replace "User:" and "AI(you):" by what you want write to indicate who's talking in the chat_history.txt
    def add_new_entry(usercontent, formatted_output):
        new_chat_history = f"User: {usercontent}\nAI(you): {formatted_output}\n"
        chat_history = open("chat_history.txt", "r").read()
        open("chat_history.txt", "w").write(chat_history + new_chat_history)

    return write_to_file, add_new_entry

write_to_file, add_new_entry = store_chat_history('chat_history.txt')
