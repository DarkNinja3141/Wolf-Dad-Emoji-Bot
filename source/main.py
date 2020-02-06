from .config import config

from discord.ext.commands import Bot

client: Bot = Bot(command_prefix=config.prefix, owner_id=config.owner)

if __name__ == "__main__":
    client.run(config.token)
