from rivescript import RiveScript

#unicode arabic
bot=RiveScript(utf8=True)

#load directories
bot.load_directory("brain")
bot.sort_replies()

def chat(message):
    if message=="":
        return -1,"no message found"
    else:
        response=bot.reply("user",message)
    if response:
        return 0, response
    else:
        return -1, "no response found"
