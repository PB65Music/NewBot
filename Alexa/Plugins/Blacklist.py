# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma



from pyrogram import Client, filters
from pyrogram.types import Message

from Alexa import SUDOERS, app
from Alexa.Database import blacklist_chat, blacklisted_chats, whitelist_chat

__MODULE__ = "🤭 ʙʟᴀᴄᴋʟɪsᴛ"
__HELP__ = """


`/blacklistedchat`
- ᴄʜᴇᴄᴋ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛs ᴏғ ʙᴏᴛ.


**ɴᴏᴛᴇ:**
ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs.


`/blacklistchat` [ᴄʜᴀᴛ_ɪᴅ] 
- ʙʟᴀᴄᴋʟɪsᴛ ᴀɴʏ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ ᴍᴜsɪᴄ ʙᴏᴛ


`/whitelistchat` [ᴄʜᴀᴛ_ɪᴅ] 
- ᴡʜɪᴛᴇʟɪsᴛ ᴀɴʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ ᴍᴜsɪᴄ ʙᴏᴛ

- ᴘᴏᴡᴇʀᴅ ʙʏ 😍 🅐𝖚𝖏𝖑𝖆 ᴀɴᴅ @Urban_Chat_Group

"""


@app.on_message(filters.command(["black", "blacklistchat"]) & filters.user(SUDOERS))
async def blacklist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "**ᴜsᴀɢᴇ:**\n/blacklistchat [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await blacklisted_chats():
        return await message.reply_text("ᴄʜᴀᴛ ɪs ᴀʟʀᴇᴀᴅʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ...")
    blacklisted = await blacklist_chat(chat_id)
    if blacklisted:
        return await message.reply_text(
            "ᴄʜᴀᴛ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ"
        )
    await message.reply_text("sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ, ᴄʜᴇᴄᴋ ʟᴏɢs...")


@app.on_message(filters.command(["white", "whitelistchat"]) & filters.user(SUDOERS))
async def whitelist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "**ᴜsᴀɢᴇ:**\n/whitelistchat [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats():
        return await message.reply_text("ᴄʜᴀᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴡʜɪᴛᴇʟɪsᴛᴇᴅ...")
    whitelisted = await whitelist_chat(chat_id)
    if whitelisted:
        return await message.reply_text(
            "ᴄʜᴀᴛ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴡʜɪᴛᴇ ʟɪsᴛᴇᴅ..."
        )
    await message.reply_text("sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ, ᴄʜᴇᴄᴋ ʟᴏɢs...")


@app.on_message(filters.command("blacklistedchat"))
async def blacklisted_chats_func(_, message: Message):
    text = "**ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛs:**\n\n"
    j = 0
    for count, chat_id in enumerate(await blacklisted_chats(), 1):
        try:
            title = (await app.get_chat(chat_id)).title
        except Exception:
            title = "Private"
        j = 1
        text += f"**{count}. {title}** [`{chat_id}`]\n"
    if j == 0:
        await message.reply_text("ɴᴏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛs")
    else:
        await message.reply_text(text)
