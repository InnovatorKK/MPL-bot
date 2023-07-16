import discord

TOKEN = ""
channelID = []

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'loggen in as {self.user}')
        
    async def on_message(self, message):
        print(f'message from {message.author}: {message.content}')
        #if message.channel.type == "public_thread":
        print(message.channel.id)
        
        if message.author.bot == False and str(message.channel.type) == "public_thread":
            if message.channel.id in channelID:
                pass
            else:
                await message.channel.send("<@&1077985851562278922>")
                channelID.append(message.channel.id)
        
    
        
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)



