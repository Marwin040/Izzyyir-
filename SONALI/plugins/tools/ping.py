from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from SONALI import app
from SONALI.core.call import RAUSHAN
from SONALI.utils import bot_sys_stats
from SONALI.utils.decorators.language import language
from SONALI.utils.inline import supp_markup
from SONALI.utils.inline import close_markup
from config import BANNED_USERS
import aiohttp
import asyncio
from io import BytesIO
from PIL import Image, ImageEnhance 
from time import time
import asyncio
from SONALI.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5
# Add these imports

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())

    # Open the image using PIL
    carbon_image = Image.open(image)

    # Increase brightness
    enhancer = ImageEnhance.Brightness(carbon_image)
    bright_image = enhancer.enhance(1.7)  # Adjust the enhancement factor as needed

    # Save the modified image to BytesIO object with increased quality
    output_image = BytesIO()
    bright_image.save(output_image, format='PNG', quality=95)  # Adjust quality as needed
    output_image.name = "carbon.png"
    return output_image

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    user_id = message.from_user.id
    current_time = time()
    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        # If less than the spam window time has passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            # Block the user if they exceed the threshold
            hu = await message.reply_text(f"**{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**")
            await asyncio.sleep(3)
            await hu.delete()
            return 
    else:
        # If more than the spam window time has passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

    PING_IMG_URL = "https://telegra.ph/file/37b57c6aaaa793bba055a.jpg"
    captionss = "**𝑊𝑎𝑖𝑡 𝑃𝑎𝑛𝑛𝑟𝑎 🥹 𝑃𝑖𝑛𝑔 𝐴𝑔𝑎𝑛𝑢𝑚 🤌🏻💙✨**"
    response = await message.reply_photo(PING_IMG_URL, caption=(captionss))
    await asyncio.sleep(1)
    await response.edit_caption("**𝑊𝑎𝑖𝑡 𝑃𝑎𝑛𝑛𝑟𝑎 🥹 𝑃𝑖𝑛𝑔 𝐴𝑔𝑎𝑛𝑢𝑚 🤌🏻💙✨...**")
    await asyncio.sleep(1)
    await response.edit_caption("**𝑊𝑎𝑖𝑡 𝑃𝑎𝑛𝑛𝑟𝑎 🥹 𝑃𝑖𝑛𝑔 𝐴𝑔𝑎𝑛𝑢𝑚 🤌🏻💙✨.**")
    await asyncio.sleep(1)
    await response.edit_caption("**𝑊𝑎𝑖𝑡 𝑃𝑎𝑛𝑛𝑟𝑎 🥹 𝑃𝑖𝑛𝑔 𝐴𝑔𝑎𝑛𝑢𝑚 🤌🏻💙✨..**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**𝑊𝑎𝑖𝑡 𝑃𝑎𝑛𝑛𝑟𝑎 🥹 𝑃𝑖𝑛𝑔 𝐴𝑔𝑎𝑛𝑢𝑚 🤌🏻💙✨...**")
    await asyncio.sleep(2)
    await response.edit_caption("**𝑊𝑎𝑖𝑡 𝑃𝑎𝑛𝑛𝑟𝑎 🥹 𝑃𝑖𝑛𝑔 𝐴𝑔𝑎𝑛𝑢𝑚 🤌🏻💙✨....**")
    await asyncio.sleep(2)
    await response.edit_caption("**𝐼𝑟𝑢 𝑅𝑎𝑠𝑎 𝐴𝑛𝑢𝑝𝑎𝑟𝑒𝑎𝑛 🤌🏻🫀**")
    await asyncio.sleep(3)
    await response.edit_caption("**𝐽𝑜𝑙𝑖 𝑀𝑢𝑑𝑢𝑛𝑗𝑢𝑡ℎ𝑢 🥹✨")
    start = datetime.now()
    pytgping = await RAUSHAN.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text =  _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    carbon = await make_carbon(text)
    captions = "** 𝐼𝑡ℎ𝑜𝑜𝑜 𝑉𝑎𝑛𝑡ℎ𝑢𝑡𝑒𝑎𝑛.....\n 𝐼𝑡ℎ𝑜𝑜𝑜 𝑉𝑎𝑛𝑡ℎ𝑢𝑡𝑒𝑎𝑛.....**"
    await message.reply_photo((carbon), caption=captions,
    reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="🍷 𝐆𖽷𖽙𖽪𖽳 😻", url=f"https://t.me/Team_Hypers_Networks",
            ),
            InlineKeyboardButton(
                text="🍷 𝐎𖾟𖽡𖽞𖾖 😻", url=f"https://t.me/king_0f_izzy",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍷 𝐇𖽞𖾘𖽳 😻", url=f"https://t.me/{app.username}?start=help"
            )
        ],
    ]
    ),
        )
    await response.delete()

    close_button = InlineKeyboardButton("🍷 𝐂𖾘𖽙𖾗𖽞 😻", callback_data="close_data")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])

@app.on_callback_query(filters.regex("^close_data"))
async def close_callback(_, query):
    chat_id = query.message.chat.id
    await query.message.delete()
