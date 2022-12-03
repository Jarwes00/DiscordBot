import platform
import pyaztro
import responses
import discord
from aztro import Aztro


async def do_horoscope(message, sign):
    try:
        # todo: get_full_message(self, string) doablent # NOQA
        byle_co = Aztro(sign) # NOQA
        await message.channel.send(byle_co.description)
        await message.channel.send(byle_co.mood)
        await message.channel.send(byle_co.compatibility)
        await message.channel.send(byle_co.lucky_number)
    except pyaztro.exceptions.PyAztroSignException:  # NOQA
        await message.channel.send("zły znak") # NOQA


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as err:
        print("Hm?", err)


def run_discord():
    TOKEN = 'MTA0ODE2MjU3ODE0MjA4NTEyMQ.Gulpr9.EcfNLFRCNJsQ30_LpO5w9oPXOupXYG3N4_NeyA' # NOQA
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("------------------------")
        print(f'{client.user} is online')
        print(f"Logged in as {client.user.name}")
        print(f"discord.py API version: {discord.__version__}")
        print(f"Python version: {platform.python_version()}")
        print(f"Running on: {platform.system()} {platform.release()}")
        print("-----------------------")

    @client.event
    async def on_message(message):
        # Debug - nie bedzie loopy # NOQA
        if message.author == client.user:
            return

        user = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        # debug
        print(f"'{user} said: '{user_message}f' ({channel})")

        if user_message.startswith("horoscope"):
            sign = user_message.split(' ')[1]
            await do_horoscope(message, sign)
        else:
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
            else:
                await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
