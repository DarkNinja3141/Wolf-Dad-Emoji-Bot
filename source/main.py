from discord.ext.commands import Bot

from config import config
from component import *

client: Bot = Bot(command_prefix=config.prefix, owner_id=config.owner)

# On ready
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == "__main__":
    client.add_cog(AdminCommands(client))
    client.run(config.token)
