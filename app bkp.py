import telebot
from telebot import types

# Leitura do arquivo de configuração
with open('config.ini', 'r') as f:
    config = f.read().splitlines()

# Criação do bot com o token do arquivo de configuração
bot = telebot.TeleBot(token=config[0], parse_mode='HTML')


# Comando Inicial
@bot.message_handler(commands=['start'])
def handler_start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton('💻 Suporte TGA', callback_data='tga'),
        types.InlineKeyboardButton('💻 Suporte XD', callback_data='xd'),
        types.InlineKeyboardButton('💻 Suporte SoftJava', callback_data='softjava'),
        types.InlineKeyboardButton('Acesse: TecnoPro Sistemas', url='http://www.tecnopro.inf.br/site/'),
        row_width=2        
    )
    bot.send_message(chat_id=message.from_user.id, text='<b>Sr(a) {}</b>, seja bem vindo, escolha uma das opções abaixo:'.format(message.from_user.first_name), reply_markup=markup)

# Criação CallBacks
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'tga':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('TGA Estoque', callback_data='tga_estoque'),
            types.InlineKeyboardButton('TGA Financeiro', callback_data='tga_financeiro'),
            row_width=2
        )
        bot.send_message(chat_id=call.from_user.id, text='<b>Sr(a) {}</b>, bem vindo ao Suporte TGA Sistemas. Favor escolher uma das opções abaixo:'.format(call.from_user.first_name), reply_markup=markup)
    elif call.data == 'xd':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('XD PDV', callback_data='xd_pdv'),
            types.InlineKeyboardButton('XD Gestão Comercial', callback_data='xd_gestao'),
            row_width=2
        )
        bot.send_message(chat_id=call.from_user.id, text='<b>Sr(a) {}</b>, bem vindo ao Suporte XD. Favor escolher uma das opções abaixo:'.format(call.from_user.first_name), reply_markup=markup)
    elif call.data == 'softjava':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('SoftJava PDV', callback_data='softjava_pdv'),
            types.InlineKeyboardButton('SoftJava Cloud', callback_data='softjava_cloud'),
            row_width=2
        )
        bot.send_message(chat_id=call.from_user.id, text='<b>Sr(a) {}</b>, bem vindo ao Suporte SoftJava. Favor escolher uma das opções abaixo:'.format(call.from_user.first_name), reply_markup=markup)

    if call.data == 'tga_estoque':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        markup_opcoes = types.InlineKeyboardMarkup()
        markup_opcoes.add(
            types.InlineKeyboardButton('Teste Imagem', callback_data='img'),
            types.InlineKeyboardButton('Teste PDF', callback_data='pdf'),
            types.InlineKeyboardButton('Teste Video', callback_data='mp4'),
            row_width=3
        )
        bot.send_message(chat_id=call.from_user.id, text='<b>Sr(a) {}</b>, escolha uma das opções abaixo:'.format(call.from_user.first_name), reply_markup=markup_opcoes)

    if call.data == 'img':
        bot.send_chat_action(chat_id=call.from_user.id, action='typing')
        bot.send_photo(chat_id=call.from_user.id, photo=open('Tutoriais/Imagens/Teste.png', 'rb'),caption='Selecionado: Tutorial de tal coisa') 

# #$ 1. TUTORIAL: Enviar Texto
# @bot.message.handler(comands=['text'])
# def handler_text(message):
#     bot.send_message(chat_id=message.from_user.id, text='Enviado com sucesso!', reply_to_message_id=message.message.id)

# #$ 2. TUTORIAL: Enviar Imagem
# @bot.message.handler(comands=['image'])
# def handler_imagem(message):
#     bot.send_photo(chat_id=message.from_user.id, photo=open('nome do arquivo.jpg', 'rb'),caption='imagem enviada corretamente', reply_to_message_id=message.message.id)

# #$ 3. TUTORIAL: Enviar audio
# @bot.message.handler(comands=['audio'])
# def handler_audio(message):
#     bot.send_audio(chat_id=message.from_user.id, audio=open('nome do arquivo.mp3', 'rb'),caption='imagem enviada corretamente', reply_to_message_id=message.message.id)

# #$ 4. TUTORIAL: Enviar documento
# @bot.message.handler(comands=['document'])
# def handler_document(message):
#     bot.send_document(chat_id=message.from_user.id, document=open('nome do arquivo.mp3', 'rb'),caption='imagem enviada corretamente', reply_to_message_id=message.message.id)

bot.polling()