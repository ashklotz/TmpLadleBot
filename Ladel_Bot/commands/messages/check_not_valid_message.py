import discord
import enums


async def respond_not_valid_message(message: discord.Message):
    message_str = message.content.lower()
    for not_valid_str in enums.NotValidStr:
        if not_valid_str.value in message_str:
            await message.reply(
                "You are in fact, loved and valid <:pride_shiny_heart_flag:1253712640321126471>"
            )
