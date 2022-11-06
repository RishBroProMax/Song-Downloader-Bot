

#😎😍💔💙❤💚💌💥👋✌🤘💻💾📓📗💡📍📌🔓🔒🔐🔏🖇🔗🛡🔮⚘🌷🌱🌲🌟☄☇🌙🌞🌝🌚☈⭐🌟☄

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup

from Bot.plugins import *

from pyrogram import idle, filters

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bot import Bot as app

from Bot import LOGGER

pm_start_text = """

👋 Hello [{}](tg://user?id={}),\n\n I'm Song Downloader Bot


⚘ Just send me the song name you want to download.😋

      eg:```/song Faded```

      

**☇Powerd By  </> ємσ вσт ∂єνσℓσρєʀѕ 🇱🇰**

**🧑‍💻 Devoloper - @ImRishmika**

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

                        text="☇ Updates", url="https://t.me/EmoBotDevolopers"

                    ),

                    InlineKeyboardButton(

                        text="☄ Support", url="https://t.me/EmoBotSupport"

                    )

                ],

                 InlineKeyboardButton(

                        text="🇱🇰 Owner", url="https://t.me/ImRishmika"

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
