from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = update.chat_member.new_chat_member.user
    chat_id = update.chat_member.chat.id

    photos = await context.bot.get_user_profile_photos(member.id, limit=1)

    caption = f"""
⭐✨ WELCOME BOT ✨⭐

👋 Hello, {member.first_name}!
🎮 Welcome to SKT GAMES GROUP

🚫 No spam | Be respectful
🤖 Powered by SKY_B.O.T
"""

    if photos.total_count > 0:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=photos.photos[0][-1].file_id,
            caption=caption
        )
    else:
        await context.bot.send_message(chat_id=chat_id, text=caption)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatMemberHandler(welcome))
app.run_polling()
