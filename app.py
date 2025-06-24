import os
import logging
import requests
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = "https://investiments-ai-c6fb384d99c9.herokuapp.com/recommend_etfs?risk_level=high"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    logger.info("User %s (%s) started the bot", user.username, user.id)
    await update.message.reply_text("Welcome to your Investment Bot! Use /recommendation to check recommendations.")

# /recommendation command handler
async def get_recommendation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user
        logger.info("User %s requested recommendation", user.username or user.id)

        response = requests.get(API_URL, timeout=20)  # timeout in seconds
        response.raise_for_status()
        data = response.json()

        raw_recommendations = data.get("recommendations", "[]")

        # Make sure it's valid JSON string inside the string
        recommendations = json.loads(raw_recommendations)

        message = "📊 *ETF Recommendations:*\n"
        for item in recommendations:
            name = item.get("name", "Unknown")
            allocation = item.get("% allocation") or item.get("allocation", "N/A")
            message += f"• {name} — *{allocation}*\n"

        await update.message.reply_text(message, parse_mode="Markdown")

    except Exception as e:
        logger.error("Error fetching or parsing: %s", e, exc_info=True)
        await update.message.reply_text("⚠️ Couldn't fetch recommendations.")

# Set up the bot application
if __name__ == "__main__":
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN must be set as environment variables")
        exit(1)

    logger.info("Starting bot...")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("recommendation", get_recommendation))

    logger.info("Bot is running...")
    app.run_polling()