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
import asyncio
from pyrogram import Client, idle, filters
import os
from config import Config
from utils import mp, USERNAME, FFMPEG_PROCESSES
from pyrogram.raw import functions, types
import os
import sys
from threading import Thread
from signal import SIGINT
import subprocess
CHAT=Config.CHAT
bot = Client(
    "Musicplayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.start_radio()
def stop_and_restart():
    bot.stop()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, *sys.argv)

bot.run(main())
bot.start()

@bot.on_message(filters.command(["restart", f"restart@{USERNAME}"]) & filters.user(Config.ADMINS) & (filters.chat(CHAT) | filters.private))
async def restart(client, message):
    await message.reply_text("🔄 Restarting...")
    await asyncio.sleep(3)
    try:
        await message.delete()
    except:
        pass
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
        except Exception as e:
            print(e)
            pass
        FFMPEG_PROCESSES[CHAT] = ""
    Thread(
        target=stop_and_restart
        ).start()    


bot.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="start",
                description="Check if bot is alive"
            ),
            types.BotCommand(
                command="assistance",
                description="Shows help message"
            ),
            types.BotCommand(
                command="p",
                description="Play song from youtube/audiofile"
            ),
            types.BotCommand(
                command="d",
                description="Play song from Deezer"
            ),
            types.BotCommand(
                command="c",
                description="Shows current playing song with controls"
            ),
            types.BotCommand(
                command="rsm",
                description="Shows the playlist"
            ),
            types.BotCommand(
                command="sk",
                description="Skip the current song"
            ),
            types.BotCommand(
                command="j",
                description="Join VC"
            ),
            types.BotCommand(
                command="l",
                description="Leave from VC"
            ),
            types.BotCommand(
                command="vc",
                description="Ckeck if VC is joined"
            ),
            types.BotCommand(
                command="st",
                description="Stops Playing"
            ),
            types.BotCommand(
                command="r",
                description="Start radio / Live stream"
            ),
            types.BotCommand(
                command="sr",
                description="Stops radio/Livestream"
            ),
            types.BotCommand(
                command="rp",
                description="Replay from beginning"
            ),
            types.BotCommand(
                command="cl",
                description="Cleans RAW files"
            ),
            types.BotCommand(
                command="pa",
                description="Pause the song"
            ),
            types.BotCommand(
                command="re",
                description="Resume the paused song"
            ),
            types.BotCommand(
                command="m",
                description="Mute in VC"
            ),
            types.BotCommand(
                command="volume",
                description="Set volume between 0-200"
            ),
            types.BotCommand(
                command="unm",
                description="Unmute in VC"
            ),
            types.BotCommand(
                command="restart",
                description="Restart the bot"
            )
        ]
    )
)

idle()
bot.stop()
