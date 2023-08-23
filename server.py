from pyrogram import Client, filters

app = Client("my_bot")


@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply("Hola este bot está en desarrollo aún")


app.run()  # Automatically start() and idle()
