import telebot
TOKEN = "8732112347:AAEXoXj7PCwK0Ezy-gAJvPO_8CpP0ZKMjpg"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    savol = bot.send_message(message.chat.id, "Salom! Men BMI botman. Ismingiz nima?")
    bot.register_next_step_handler(savol, get_name)
def get_name(message):
    ism = message.text
    savol = bot.send_message(message.chat.id, f"Tanishganimdan xursandman, {ism}! Vazningizni kiriting (kg):")
    bot.register_next_step_handler(savol, get_weight, ism)
def get_weight(message, ism):
    try:
        vazn = float(message.text)
        savol = bot.send_message(message.chat.id, "Endi bo'yingizni kiriting (metrda, masalan 1.75):")
        bot.register_next_step_handler(savol, calculate_bmi, ism, vazn)
    except ValueError:
        savol = bot.send_message(message.chat.id, "Xato! Vaznni sonda kiriting (masalan: 70.5):")
        bot.register_next_step_handler(savol, get_weight, ism)
def calculate_bmi(message, ism, vazn):
    try:
        boy = float(message.text)
        bmi = vazn / (boy ** 2)
        
        if bmi < 18.5:
            holat = "Vazn yetishmaydi 🍎"
        elif 18.5 <= bmi < 25:
            holat = "Vazningiz normal ✅"
        else:
            holat = "Vazn ortiqcha 🏃‍♂️"
            
        natija = (f"Hurmatli {ism}!\n"
                  f"Sizning BMI: {bmi:.1f}\n"
                  f"Holatingiz: {holat}\n"
                  f"Norma: 18.5 - 25")
        
        bot.send_message(message.chat.id, natija)
    except ValueError:
        savol = bot.send_message(message.chat.id, "Xato! Bo'yni sonda kiriting (masalan: 1.8):")
        bot.register_next_step_handler(savol, calculate_bmi, ism, vazn)
@bot.message_handler(func=lambda message:"seni kim yasagan" in message.text.lower())
def creator(message):
       bot.send_message(message.chat.id, "Meni Mansurbek Makhmudov Madiyorjonovich yasagan! 😎")
bot.polling(none_stop=True)
