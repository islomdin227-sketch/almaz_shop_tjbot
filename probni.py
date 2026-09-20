import asyncio
import os
import re
import random
import string
import sqlite3
from datetime import datetime
import requests
from PIL import Image
import pytesseract
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# ===================== ТАНЗИМОТИ АСОСӢ (МУСТАҚИМ ДАР ДОХИЛ) =====================
TOKEN = "8668882369:AAH1xzGFI9DMm5aKasBIb6gOvSroAusp3u0"
ADMIN_TELEGRAM_ID = 8727925331

FIRELOOT_KEY = "fl_live_Er5dlM-JzL7sMIwW4k25IGpchsA6r3toqw21ysS9tho"
FIRELOOT_BASE = "https://partner.firelootshop.com/api/v1"

WHATSAPP_PHONE = "992933313738"
WHATSAPP_APIKEY = "5444428"
DC_CARD = "9762000001085389"
ALIF_ACCOUNT = "933313738"

CHANNEL_USERNAME = "@ffalmaz_shop_tj"

# ===================== Telethon (ҳатто агар TELETHON_ENABLED=False бошад) =====================
API_ID = 33314650
API_HASH = "69c7be45f3960832adef665de2733c55"
DC_BOT_USERNAME = "@almaz_shop_tjbot"
TELETHON_SESSION = "almaz_dc_session"

# ===================== БОҚИИ КОД (ҳамон хел) =====================
user_data = {}
pending_orders = {}
known_users = set()
bot_app = None

# ... (ҳамаи қисмҳои дигар ҳамон хел мемонанд — боғайра, пакетҳо, клавиатураҳо, handlers ва ғайра)

# ===================== MAIN =====================
def main():
    validate_packages_against_fireloot()

    application = Application.builder().token(TOKEN).build()

    # ... (ҳамаи handlerҳо ҳамон хел)

    async def post_init(app: Application):
        await app.bot.delete_webhook(drop_pending_updates=True)
        print("✅ Webhook тоза шуд")

    application.post_init = post_init

    print("🤖 Бот ALMAZ TJ бо тағйиротҳои мустақим оғоз шуд!")
    application.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()