#########################################################
# BT Channel Re-poster: http://t.me/channel_reposter_bot
# Per creare/configurare un bot: https://t.me/BotFather
# Per conoscere l'ID di un canale: https://t.me/getidsbot
#########################################################

from datetime import datetime
import pytz
import os
from telegram import Update, constants, helpers as h, MessageEntity as me, File as tf
from telegram.ext import Application, ContextTypes, MessageHandler, filters
import io

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

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.channel_post
    if message:
        if (message.chat_id == ORIGIN_CHANNEL_ID):
            if POST_AS_NEW_MSG:
            ################################
            # INVIO POST IMMAGINE E TESTO 
            ################################
                if message.photo:
                    file_id = message.photo[-1].file_id  # -1 to get the photo of the best quality
                    if file_id:
                        print("[" + get_iso_rome_datetime() + "] Msg received with IMAGE from " + str(message.chat_id))
                        caption = message.caption
                        if caption and (len(caption) > constants.MessageLimit.CAPTION_LENGTH):
                            print("[" + get_iso_rome_datetime() + "] [ERROR] Image caption too long. Post not sent.")
                            return None

                        # Ottieni l'immagine come un oggetto file
                        photo_file: tf = await context.bot.get_file(file_id)

                        # Crea un oggetto BytesIO dalla tua foto
                        photo_data = io.BytesIO()
                        await photo_file.download_to_memory(out = photo_data)
                        photo_data.seek(0)
                        
                        await context.bot.send_photo    (
                                                            chat_id = DESTINATION_CHANNEL_ID, 
                                                            photo = photo_data, 
                                                            caption = caption,
                                                            disable_notification = DISABLE_MSG_NOTIFICATION
                                                        )
                        return None
                    
            ################################
            # INVIO POST ANIMAZIONE E TESTO 
            ################################
                if message.animation:
                    file_id = message.animation.file_id
                    if file_id:
                        print("[" + get_iso_rome_datetime() + "] Msg received with ANIMATION from " + str(message.chat_id))
                        caption = message.caption
                        if caption and (len(caption) > constants.MessageLimit.CAPTION_LENGTH):
                            print("[" + get_iso_rome_datetime() + "] [ERROR] Animation caption too long. Post not sent.")
                            return None
                        await context.bot.send_animation    (
                                                            chat_id = DESTINATION_CHANNEL_ID, 
                                                            animation = message.animation, 
                                                            caption = caption,
                                                            disable_notification = DISABLE_MSG_NOTIFICATION
                                                        ) 
                        return None

            ################################
            # INVIO POST FILE E TESTO 
            ################################
                if message.document:
                    file_id = message.document.file_id
                    if file_id:
                        print("[" + get_iso_rome_datetime() + "] Msg received with FILE from " + str(message.chat_id))
                        caption = message.caption
                        if caption and (len(caption) > constants.MessageLimit.CAPTION_LENGTH):
                            print("[" + get_iso_rome_datetime() + "] [ERROR] File caption too long. Post not sent.")
                            return None
                        await context.bot.send_document (
                                                            chat_id = DESTINATION_CHANNEL_ID, 
                                                            document = message.document, 
                                                            caption = caption,
                                                            disable_notification = DISABLE_MSG_NOTIFICATION
                                                        )                        
                        return None
                    
            ################################
            # INVIO POST VOCALE E TESTO 
            ################################
                if message.voice:
                    file_id = message.voice.file_id
                    if file_id:
                        print("[" + get_iso_rome_datetime() + "] Msg received with VOCAL from " + str(message.chat_id))
                        caption = message.caption
                        if caption and (len(caption) > constants.MessageLimit.CAPTION_LENGTH):
                            print("[" + get_iso_rome_datetime() + "] [ERROR] Vocal caption too long. Post not sent.")
                            return None
                        await context.bot.send_voice    (
                                                            chat_id = DESTINATION_CHANNEL_ID, 
                                                            voice = message.voice, 
                                                            caption = caption,
                                                            disable_notification = DISABLE_MSG_NOTIFICATION
                                                        )                        
                        return None
                    
            ################################
            # INVIO POST AUDIO E TESTO 
            ################################
                if message.audio:
                    file_id = message.audio.file_id
                    if file_id:
                        print("[" + get_iso_rome_datetime() + "] Msg received with AUDIO from " + str(message.chat_id))
                        caption = message.caption
                        if caption and (len(caption) > constants.MessageLimit.CAPTION_LENGTH):
                            print("[" + get_iso_rome_datetime() + "] [ERROR] Audio caption too long. Post not sent.")
                            return None
                        await context.bot.send_audio    (
                                                            chat_id = DESTINATION_CHANNEL_ID, 
                                                            audio = message.audio, 
                                                            title = message.audio.title, 
                                                            caption = caption,
                                                            disable_notification = DISABLE_MSG_NOTIFICATION
                                                        ) 
                        return None
                    
            ################################
            # INVIO POST VIDEO E TESTO 
            ################################
                if message.video:
                    file_id = message.video.file_id
                    if file_id:
                        print("[" + get_iso_rome_datetime() + "] Msg received with VIDEO from " + str(message.chat_id))
                        caption = message.caption
                        if caption and (len(caption) > constants.MessageLimit.CAPTION_LENGTH):
                            print("[" + get_iso_rome_datetime() + "] [ERROR] Audio caption too long. Post not sent.")
                            return None
                        await context.bot.send_video    (
                                                            chat_id = DESTINATION_CHANNEL_ID, 
                                                            video = message.video, 
                                                            caption = caption,
                                                            disable_notification = DISABLE_MSG_NOTIFICATION
                                                        ) 
                        return None

            ################################
            # INVIO POST SOLO TESTO 
            ################################
                if message.text:
                    print("[" + get_iso_rome_datetime() + "] Msg received: " + message.text + " from " + str(message.chat_id))
                    if len(message.text) > constants.MessageLimit.MAX_TEXT_LENGTH:
                        print("[" + get_iso_rome_datetime() + "] [ERROR] Text too long. Post not sent.")
                        return None
                    await context.bot.send_message  (
                                                        chat_id = DESTINATION_CHANNEL_ID,
                                                        text = escape_msg_text(message.text + MSG_SIGNATURE),
                                                        parse_mode = constants.ParseMode.MARKDOWN_V2,
                                                        disable_notification = DISABLE_MSG_NOTIFICATION
                                                    )
                    return None
            else:
                print("[" + get_iso_rome_datetime() + "] Msg received for FOWARDING from " + str(message.chat_id))
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