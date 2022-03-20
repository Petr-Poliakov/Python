from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from log import *

def Hi_command(update: Update, context: CallbackContext):
    log_command(update,context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def time_command(update: Update, context: CallbackContext):
    log_command(update,context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def help_command(update: Update, context: CallbackContext):
    log_command(update,context)
    update.message.reply_text(f'/hello\n/time\n/help\n/sum')

def echo_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    update.message.reply_text(f'{msg}')

def sum_command(update: Update, context: CallbackContext):
    log_command(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum  123 321 
    x = int (items[1])
    y = int (items[2])
    update.message.reply_text(f'{x}+{y}={x+y}')