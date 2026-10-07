```python
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


# Bot起動時
@bot.event
async def on_ready():
    print(f"{bot.user} でログインしました")


# メッセージを送ったとき
@bot.event
async def on_message(message):
    # Bot自身のメッセージは無視
    if message.author.bot:
        return

    # #bot-logs を探す
    log_channel = discord.utils.get(message.guild.text_channels, name="bot-logs")

    if log_channel:
        await log_channel.send(
            f"📩 **メッセージログ**\n"
            f"ユーザー：{message.author.mention}\n"
            f"チャンネル：#{message.channel.name}\n"
            f"内容：{message.content}"
        )

    # コマンドを動かすために必要
    await bot.process_commands(message)


# !ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


bot.run(os.environ["DISCORD_TOKEN"])
```
