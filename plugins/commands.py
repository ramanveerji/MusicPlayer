#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Hello, [{}](tg://user?id={})\n\n• I am A RS DJ BOT\n• I Can Manage Group VC's\n\n• Hit /assistance to know about available commands.</b>"
HELP = """

<b>Add the bot and User account in your Group with admin rights.

Start a VoiceChat.

Use /play <song name> or use /play as a reply to an audio file or youtube link.

You can also use /dplay <song name> to play a song from Deezer.</b>

**Common Commands**:

**/p**  Reply to an audio file or YouTube link to play it or use /p <song name>.
**/d** Play music from Deezer, Use /d <song name>
**/c**  Show current playing song.
**/assistance** Show help for commands
**/rsm** Shows the playlist.

**Admin Commands**:
**/sk** [n] ...  Skip current or n where n >= 2
**/j**  Join voice chat.
**/l**  Leave current voice chat
**/rs**  Check which VC is joined.
**/st**  Stop playing.
**/r** Start Radio.
**/sr** Stops Radio Stream.
**/rp**  Play from the beginning.
**/cl** Remove unused RAW PCM files.
**/pa** Pause playing.
**/re** Resume playing.
**/volume** Change volume(0-200).
**/m**  Mute in VC.
**/unm**  Unmute in VC.
**/restart** Restarts the Bot.
"""



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
    [
                InlineKeyboardButton('🎭 Our Channel 🎭️', url='https://t.me/rsbro'),
            ],
            [
                InlineKeyboardButton('🤖 Admin', url='https://t.me/ramanveerji'),
                InlineKeyboardButton('🎟️ Discussion Group', url='https://t.me/joinchat/QsoZgoV2oveZZBCn'),
            ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)



@Client.on_message(filters.command(["assistance", f"assistance@{U}"]))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('🎭 Our Channel 🎭️', url='https://t.me/rsbro'),
            ],
            [
                InlineKeyboardButton('🤖 Admin', url='https://t.me/ramanveerji'),
                InlineKeyboardButton('🎟️ Discussion Group', url='https://t.me/joinchat/QsoZgoV2oveZZBCn'),
            ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('assistance') is not None:
        await msg['assistance'].delete()
    msg['assistance'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await mp.delete(message)
