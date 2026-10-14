import os
import asyncio
from rubika_bot_api.api import Robot
from rubika_bot_api import filters

TOKEN = os.environ.get("RUBIKA_TOKEN")
if not TOKEN:
    raise RuntimeError("RUBIKA_TOKEN is not set")

bot = Robot(token=TOKEN)

WELCOME = """سلام رفیق! 👋🔥
به ربات XMG CITY خوش اومدی! 💜

اینجا می‌تونی با سرور XMG CITY آشنا بشی🏖
برای راهنمایی بیشتر، دستور /help رو بفرست⚓"""

HELP = """⚓ راهنمای ربات XMG CITY

/start — پیام خوشامدگویی
/help — نمایش همین راهنما"""

@bot.on_message(filters=filters.pv & filters.text)
async def handle_message(bot_instance, message):
    text = (message.text or "").strip()
    if text == "/start":
        await message.reply(WELCOME)
    elif text == "/help":
        await message.reply(HELP)

if __name__ == "__main__":
    asyncio.run(bot.run())
