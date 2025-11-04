from osonbot import Bot
bot = Bot("8380176186:AAEwFZLcl_kGkQi8WLhQrCtFZD4EdxnMhms")

bot.when("/start", "Hello *{first_name}*", parse_mode="MarkdownV2", reply_markup={'inline_keyboard': [[{'text': 'yes', 'callback_data': 'yes'}, {'text': 'no', 'callback_data': 'no'}]]})
bot.when("/help", "How can i help you", parse_mode="None", reply_markup=None)
bot.when("add", "nima qo'shmoqchisiz", parse_mode="None", reply_markup=None)
bot.when("*", "{message_text}", parse_mode="None", reply_markup=None)

bot.run()