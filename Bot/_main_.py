

#😎😍💔💙❤💚💌💥👋✌🤘💻💾📓📗💡📍📌🔓🔒🔐🔏🖇🔗🛡🔮⚘🌷🌱🌲🌟☄☇🌙🌞🌝🌚☈⭐🌟☄

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from Bot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot import Bot as app
from Bot import LOGGER

pm_start_text = """

👋 Hello [{}](tg://user?id={}),

I'm TG YT Music Downloader Bot
I have been created by **Emo Bot Developers** and **SDBOTS Infinity** to download Christmas Songs for you this Christmas.
⚘ Just send me the song name you want to download.😋

      eg:```/song Faded```

**🔥Powerd By - [</> ємσ вσт ∂єνσℓσρєʀѕ](t.me/EmoBotDevolopers) & [SD Bots](t.me/SDBOTs_inifinity)**
**🧑‍💻Devoloper - @ImRishmika**

"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="☃️━━━━━━Merry Christmas━━━━━━☃️", url="https://www.youtube.com/watch?v=XaJaztbTugo"
                    )
                ],
                  [
                     InlineKeyboardButton(
                        text="🔥ємσ вσт ∂єνσℓσρєʀѕ", url="https://t.me/EmoBotDevolopers"
                    ),
                    InlineKeyboardButton(
                        text="🍁SD Bots", url="https://t.me/SDBOTS_Inifinity"
                    )
                ],
                 InlineKeyboardButton(
                        text="🧑‍💻Owner", url="https://t.me/ImRishmika"
                    )
                ],
                   InlineKeyboardButton(
                        text="🔥 Youtube 🔥", url="https://youtube.com/@Rish_Bro"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

app.start()
LOGGER.info("✅ Your Bot is Connected On Emo Network")
idle()
