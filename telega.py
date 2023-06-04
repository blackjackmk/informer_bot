import telebot
import requests
# pip install requests
from bs4 import BeautifulSoup
# pip install beautifulsoup4
# pip install lxml
import re
# pip install schedule
import schedule
import time
from time import sleep
#! /.local/bin python3
# -*- coding: utf-8 -*-

bot = telebot.TeleBot("bot_token")

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, 'I will help you')
def job():
    r = requests.get('http://zsp1.tarnobrzeg.pl/zas.html')
    r.encoding = 'utf8'
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find_all("td", string=re.compile("3 TI"))
    heads = []
    for i in head:
        f = i.get_text("\r\n", strip=True).encode()
        heads.append(f)
    i = 0
    k = len(heads) - 1
    if k == -1:
        bot.send_message(461964422, "You have not any changes")
    else:
        while i <= k:
            bot.send_message(461964422, heads[i])
            i += 1

schedule.every().day.at("05:30").do(job)
schedule.every().day.at("18:30").do(job)
job()

while True:
    schedule.run_pending()
    time.sleep(1)

bot.polling()
