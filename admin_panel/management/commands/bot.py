import datetime

from django.core.management.base import BaseCommand
from django.shortcuts import redirect

from telebot import types
import telebot
from .config import TOKEN

from admin_panel.models import *

from django.contrib import admin


ID = 0
bot = telebot.TeleBot(TOKEN)


class TaskAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        users = Profile.objects.all()
        task_list = TaskList.objects.filter(task=obj).exists()
        if not task_list:
            for user in users:
                markup = types.InlineKeyboardMarkup(row_width=1)
                click = types.InlineKeyboardButton(
                    text='Перейти', url=obj.url) #callback_data='clicked')
                markup.add(click)
                bot.send_message(
                    user.user_id, f'{obj.text}', reply_markup=markup)
            TaskList.objects.create(task=obj)



#--------------------#START#--------------------#
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    balance = Profile.objects.get(user_id=chat_id).balance
    print('ID: ' + str(chat_id))
    username = message.chat.username
    print('Username: ' + str(username))
    first_name = message.chat.first_name
    print('First name: ' + str(first_name))
    last_name = message.chat.last_name
    print('Last name: ' + str(last_name))
    print('Balance: ' + str(balance))
    print()
    p, _ = Profile.objects.get_or_create(
        user_id=chat_id,
        defaults={
            'username': username,
        }
    )
    p.save()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    balance_button = types.KeyboardButton('Баланс')
    output_button = types.KeyboardButton("Вывод средств")
    markup.add(balance_button, output_button)
    bot.send_message(message.chat.id, "Вас приветствует бот созданный компанией Oracle Digital!".format(
        message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


#--------------------#BUTTONS#--------------------#
@bot.message_handler()
def commands(message):
    chat_id = message.chat.id
    balance = Profile.objects.get(user_id=chat_id)

    if message.text == 'Баланс':
        bot.send_message(message.chat.id, f'Ваш баланс: {balance.balance} KGS')

    elif message.text == "Вывод средств":
        msg = bot.reply_to(message, 'Введите сумму вывода')
        bot.register_next_step_handler(msg, amount)


#------------------SEND_TASKS---------------------#

def send_task(message):
    tasks = Task.objects.all()
    users = Profile.objects.all()
    for task in tasks:
        task_list = TaskList.objects.filter(task=task).exists()
        if not task_list:
            for user in users:
                markup = types.InlineKeyboardMarkup(row_width=1)
                click = types.InlineKeyboardButton(
                    text='Перейти', url=task.url) #callback_data='clicked')
                markup.add(click)
                bot.send_message(
                    user.user_id, f'{task.text}', reply_markup=markup)
            TaskList.objects.create(task=task)


AMOUNT = 0
#--------------NEXT STEP HANDLERS---------------#
def amount(message):
    global AMOUNT
    amountt = message.text
    AMOUNT = amountt
    chat_id = message.chat.id
    profile = Profile.objects.get(user_id=chat_id)
    sum = profile.balance
    if sum < float(amountt):
        print(amountt)
        bot.send_message(message.chat.id, 'Недостаточно средств для вывода')
    else:
        payment = Payment(
            profile=profile,
            user_id=chat_id,
            amount=amountt,
            date=datetime.datetime.now()
        )
        payment.save()
        msg = bot.send_message(message.chat.id, 'Введите номер телефона')
        print(amountt)
        bot.register_next_step_handler(msg, number)


def number(message):
    chat_id = message.chat.id
    print(chat_id)
    phone_number = message.text
    num = Payment.objects.get(user_id=chat_id, is_active=True)
    num.number = phone_number
    num.save()
    balance = Profile.objects.get(user_id=message.chat.id)
    balance.balance -= float(AMOUNT)
    print (AMOUNT)
    balance.save()
    bot.send_message(
        message.chat.id, 'Ваша заявка успешно отправлено администратору, они посмотрят заявку в ближащее время')

    print(phone_number)


#--------------------########--------------------#
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.text == 'Перейти':
                # if call.data == 'clicked':
                tasks = Task.objects.all()
                task_list = TaskList.objects.all()
                for task in tasks:
                    if task_list:
                        our_task = task
                bon = our_task.bon
                print (bon) 
                balance = Profile.objects.get(user_id=call.message.chat.id)
                balance.balance += bon
                balance.save()
                bot.send_message(call.message.chat.id,
                                    f'Ваш баланс: {balance.balance}')
                print('Пользователь : ' + str(balance) + ' выполнил задание')

                bot.edit_message_text(chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    text="Выполнено✔",
                                    reply_markup=None)

    except Exception as e:
        print(repr(e))


class Command(BaseCommand):
    help = 'Telegram-Bot'

    def handle(self, *args, **options):
        print('Бот запущен!')
        bot.polling(none_stop=True)


tasks = Task.objects.all()
send_task(tasks)
