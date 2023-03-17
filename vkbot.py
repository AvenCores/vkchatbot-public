#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from sys import platform

from botapiconfig import myapikey

session = vk_api.VkApi(token=myapikey)

keyboard = VkKeyboard(one_time=False, inline=False)

keyboard.add_button('Меню', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Команды', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('Тех. поддержка', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('Free Telegram ChatGPT and DALLE-2 Bot', color=VkKeyboardColor.POSITIVE)


def sendmessage(userid, message):
    session.method("messages.send", {
        "user_id": userid,
        "message": message,
        "keyboard": keyboard.get_keyboard(),
        "random_id": 0
    })


def mainvkbot():
    for event in VkLongPoll(session).listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                text = event.text.lower()
                userid = event.user_id

                firstmessage = """👋 Добро пожаловать в сообщество по тематике ChatGPT! 🎉 Мы рады видеть вас здесь. 🤗 Наша цель - предоставить жителям стран СНГ простой доступ к информации из ChatGPT.

⚠️Внимание!⚠️
Пожалуйста, будьте осторожны при отправке сообщений в этом сообществе. Особенностью этого сообщества является то, что создатель сообщества может просматривать все сообщения, отправленные в нем. Пожалуйста, будьте внимательны и выскажитесь только теми словами и мыслями, которые вы готовы делиться публично. Спасибо за понимание.

---💲Реклама💲---
🔽Наш бесплатный Telegram Bot ChatGPT и DALLE-2🔽
https://t.me/avencoreschatgpt_bot
---💲Реклама💲---

❗ ️В самом сообществе нету ChatGPT! Он находится по ссылке выше, а именно в моем телеграм боте.

Чтобы вызвать список команд напиши <<Команды>>. 💬"""

                botcommands = """🤖 Список доступных команд:

(ВВОДИТЬ КОМАНДУ НУЖНО БЕЗ ТИРЕ И БЕЗ ЭМОДЗИ)

- Как зарегистрировать аккаунт аккаунт OpenAI для использования ChatGPT 🤔
- Купить рекламный пост в данном сообществе 💰
- Как задать вопрос ChatGPT 🤖❓
- Что такое ChatGPT 🤖❓
- Полезные статьи 📚
- Напиши курсовую 📝
- Напиши дипломную работу 🎓
- Напиши сочинение ✍️
- Напиши эссе 📝

- Статус бота 🤖"""
                antidolbaeb = "---💲Реклама💲---\n🔽Наш бесплатный Telegram Bot ChatGPT и DALLE-2🔽 " \
                              "https://t.me/avencoreschatgpt_bot\n---💲Реклама💲---\n\n" \
                              "ChatGPT это не волшебная палочка и он не может ничего написать с самого нуля. Чтобы в " \
                              "этом убедиться прочитайте данную статью: \n\n " \
                              "https://vk.com/@chatgptcontent-ei-chatgpt-napishi-mne-esse-sochinenie-i-esche-diplom-v-stil"
                sochinenie = "---💲Реклама💲---\n🔽Наш бесплатный Telegram Bot ChatGPT и DALLE-2🔽" \
                             "https://t.me/avencoreschatgpt_bot\n---💲Реклама💲---\n\n Или же " \
                             "просто напиши тему сочинения и ожидайте ответа от Администратора сообщества!"
                addAD = """Заполни анкету:
1) Что вы хотите прорекламировать (Ссылку и описание).
2) Предложите цену (не будьте скупы, вы в любом случае окупитесь).
3) Описание рекламного поста (по желанию, т.к я сам могу написать).

После заполнения анкеты ожидайте ответа от Администратора сообщества."""
                stargrup = "Все наши статьи являются полезными и очень информативными. Вы можете прочитать их " \
                           "абсолютно бесплатно, просто перейдите по данной ссылке: \n\n https://vk.com/@chatgptcontent"
                regacc = "https://vk.com/@chatgptcontent-registriruem-akkaunt-openai"
                vopros = "---💲Реклама💲---\n🔽Наш бесплатный Telegram Bot ChatGPT и DALLE-2🔽 " \
                         "https://t.me/avencoreschatgpt_bot\n---💲Реклама💲---\n\n" \
                         "Или же просто напиши свой вопрос и ожидай ответа."
                chatgptthis = "ChatGPT - это модель языкового обработки, разработанная OpenAI. Она была обучена на " \
                              "множестве текстов и может генерировать тексты, отвечать на вопросы и выполнять другие " \
                              "задачи обработки языка."
                botstatus = datetime.now().strftime(f"""Бот работает в штатном режиме. 🤖\n
Время: %H:%M:%S ⏰
Дата: %d.%m.%y 📅

Система: {platform} 💻
    """)
                addbottg = "---💲Реклама💲---\n🔽Наш бесплатный Telegram Bot ChatGPT и DALLE-2🔽 https://t.me/avencoreschatgpt_bot\n---💲Реклама💲---"

                texsupport = "💬 Я в VK: https://vk.com/avencores\n💬 Я в Telegram: https://t.me/avencores"

                dolbaebdetected = "Чтобы попасть в главное меню напиши <<Меню>>. \n\nЕсли вы реально пытаетесь задать вопрос в данное сообщество, то вы ДОЛБАЕБ и как личность НИКТО. Написано же, что в самом сообществе нету ChatGPT! Он находится по ссылке ниже, а именно в моем телеграм боте. \n\n---💲Реклама💲---\n🔽Наш бесплатный Telegram Bot ChatGPT и DALLE-2🔽\nhttps://t.me/avencoreschatgpt_bot\n---💲Реклама💲---"

                if text == "начать":
                    sendmessage(userid, firstmessage)

                elif text == "привет":
                    sendmessage(userid, firstmessage)

                elif text == "start":
                    sendmessage(userid, firstmessage)

                elif text == "/начать":
                    sendmessage(userid, firstmessage)

                elif text == "меню":
                    sendmessage(userid, firstmessage)

                elif text == "/меню":
                    sendmessage(userid, firstmessage)

                elif text == "/привет":
                    sendmessage(userid, firstmessage)

                elif text == "/start":
                    sendmessage(userid, firstmessage)

                elif text == "напиши курсовую":
                    sendmessage(userid, antidolbaeb)

                elif text == "напиши дипломную работу":
                    sendmessage(userid, antidolbaeb)

                elif text == "напиши сочинение":
                    sendmessage(userid, sochinenie)

                elif text == "напиши эссе":
                    sendmessage(userid, antidolbaeb)

                elif text == "купить рекламный пост в данном сообществе":
                    sendmessage(userid, addAD)

                elif text == "команды":
                    sendmessage(userid, botcommands)

                elif text == "полезные статьи":
                    sendmessage(userid, stargrup)

                elif text == "как зарегистрировать аккаунт аккаунт openai для использования chatgpt":
                    sendmessage(userid, regacc)

                elif text == "как задать вопрос chatgpt":
                    sendmessage(userid, vopros)

                elif text == "что такое chatgpt":
                    sendmessage(userid, chatgptthis)

                elif text == "статус бота":
                    sendmessage(userid, botstatus)

                elif text == "free telegram chatgpt and dalle-2 bot":
                    sendmessage(userid, addbottg)

                elif text == "тех. поддержка":
                    sendmessage(userid, texsupport)

                else:
                    sendmessage(userid, dolbaebdetected)


while True:
    try:
        mainvkbot()
    except Exception:
        continue
