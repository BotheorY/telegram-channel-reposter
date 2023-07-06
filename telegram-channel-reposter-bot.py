#########################################################
# BT Channel Re-poster: http://t.me/channel_reposter_bot
# Per creare/configurare un bot: https://t.me/BotFather
# Per conoscere l'ID di un canale: https://t.me/getidsbot
#########################################################

from datetime import datetime
import pytz
import os
from telegram import Update, constants, helpers as h, MessageEntity as me
from telegram.ext import Application, ContextTypes, MessageHandler, filters

POST_AS_NEW_MSG = True
DISABLE_MSG_NOTIFICATION = True
MSG_SIGNATURE = " \n\n----- \nCanale 👉 T.ME/SCIENZACOSCIENZA \nInformazione LIBERA per la Nuova Umanità💚 \n"

def get_bot_token() -> str:
    return os.environ.get('BT_TELEGRAM_CNL_REP_BOT_TOKEN').strip()

def get_origin_channel_id() -> int:
    return int(os.environ.get('BT_TELEGRAM_CNL_REP_BOT_SRC_CNL').strip())

def get_destination_channel_id() -> int:
    return int(os.environ.get('BT_TELEGRAM_CNL_REP_BOT_TRGT_CNL').strip())

TOKEN = get_bot_token()
ORIGIN_CHANNEL_ID = get_origin_channel_id()
DESTINATION_CHANNEL_ID = get_destination_channel_id()

def get_iso_rome_datetime() -> str:
    rome_tz = pytz.timezone('Europe/Rome')
    now = datetime.now(rome_tz).isoformat()
    return now[:19].replace("T", " ")

def escape_msg_text(msg: str) -> str:
    return h.escape_markdown(msg, 2, me.ALL_TYPES)

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post
    if message:
        if (message.chat_id == ORIGIN_CHANNEL_ID) and message.text:
            print("[" + get_iso_rome_datetime() + "] Msg received: " + message.text + " from " + str(message.chat_id))
            if POST_AS_NEW_MSG:
                await context.bot.send_message  (
                                                    chat_id = DESTINATION_CHANNEL_ID,
                                                    text = escape_msg_text(message.text + MSG_SIGNATURE),
                                                    parse_mode = constants.ParseMode.MARKDOWN_V2,
                                                    disable_notification = DISABLE_MSG_NOTIFICATION
                                                )
            else:
                await context.bot.forward_message   (
                                                        chat_id = DESTINATION_CHANNEL_ID,
                                                        from_chat_id = ORIGIN_CHANNEL_ID,
                                                        message_id = message.message_id
                                                    )

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on non command i.e message - echo the message on Telegram
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.ALL, forward))

    print("[" + get_iso_rome_datetime() + "] Started")

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()