import telebot
from telebot import types
import re

# Leitura do arquivo de configuração
with open('config.ini', 'r') as f:
    config = f.read().splitlines()

# Criação do bot com o token do arquivo de configuração
bot = telebot.TeleBot(token=config[0], parse_mode='HTML')

# Handler para o comando start
@bot.message_handler(commands=['start', 'Start']) # -> iniciar com o comando /start
@bot.message_handler(func=lambda message: message.text.lower() == 'start') # -> iniciar com o texto start
def handler_start(message):
    markup = create_menu_markup()
    bot.send_message(chat_id=message.from_user.id, text='<b>Sr(a) {}</b>, seja bem vindo, escolha uma das opções abaixo:'.format(message.from_user.first_name), reply_markup=markup)

# Callbacks TGA   
# CallBack Menu Inicial
@bot.callback_query_handler(func=lambda call: call.data == 'tga')
def suporteTga(call):
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    markup = create_menu_tga()
    bot.send_message(chat_id=call.from_user.id, text='Você selecionou -> Suporte TGA Sistemas. Favor escolher uma das opções abaixo:', reply_markup=markup)

# CallBack TGA Estoque
@bot.callback_query_handler(func=lambda call: call.data == 'tga_estoque')
def suporte_tga_estoque(call):
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    markup = create_menu_tga_estoque()
    bot.send_message(chat_id=call.from_user.id, text='Você selecionou -> TGA Estoque. Favor escolher uma das opções abaixo:', reply_markup=markup)

# CallBack TGA Financeiro
@bot.callback_query_handler(func=lambda call: call.data == 'tga_financeiro')
def suporte_tga_financeiro(call):
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    markup = create_menu_tga_financeiro()
    bot.send_message(chat_id=call.from_user.id, text='Você selecionou -> TGA Financeiro. Favor escolher uma das opções abaixo:', reply_markup=markup)



# CallBack XD
# CallBack Menu Inicial
@bot.callback_query_handler(func=lambda call: call.data == 'xd')
def suporteXd(call):
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    markup = create_menu_xd()
    bot.send_message(chat_id=call.from_user.id, text='Você selecionou -> Suporte XD Gestão. Favor escolher uma das opções abaixo:', reply_markup=markup)

# CallBack SoftJava
# CallBack Menu Inicial
@bot.callback_query_handler(func=lambda call: call.data == 'softjava')
def suporteSoftJava(call):
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    markup = create_menu_sofjava()
    bot.send_message(chat_id=call.from_user.id, text='Você selecionou -> Suporte SoftJava. Favor escolher uma das opções abaixo:', reply_markup=markup)    

# CallBack Menu Anterior
@bot.callback_query_handler(func=lambda call: call.data == 'menu_inicial')
def menu_inicial(call):
    bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    markup = create_menu_markup()
    bot.send_message(chat_id=call.from_user.id, text='Escolha uma das opções abaixo:', reply_markup=markup)

# CallBack Menu Tga    
# @bot.callback_query_handler(func=lambda call: call.data == 'menu_tga')

# FUNÇÕES

# Menu Principal
# Função para criar o markup do menu
def create_menu_markup(): 
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton('💻 Suporte TGA', callback_data='tga'),
        types.InlineKeyboardButton('💻 Suporte XD', callback_data='xd'),
        types.InlineKeyboardButton('💻 Suporte SoftJava', callback_data='softjava'),
        types.InlineKeyboardButton('Acesse: TecnoPro Sistemas', url='http://www.tecnopro.inf.br/site/'),
        row_width=2        
    )
    return markup

# Menus TGA
# Função para criar o markup do menu TGA
def create_menu_tga():
    markup = types.InlineKeyboardMarkup()
    markup.add(
            types.InlineKeyboardButton('TGA Estoque', callback_data='tga_estoque'),
            types.InlineKeyboardButton('TGA Financeiro', callback_data='tga_financeiro'),
            types.InlineKeyboardButton('Menu Anterior', callback_data='start'),
            row_width=2
        )
    return markup

# Função para criar o markup do menu TGA Estoque
def create_menu_tga_estoque():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton('Receber Imagem', callback_data='img'),
        types.InlineKeyboardButton('Receber PDF', callback_data='pdf'),
        types.InlineKeyboardButton('Receber Video', callback_data='mp4'),
        types.InlineKeyboardButton('Receber Audio', callback_data='mp3'),
        types.InlineKeyboardButton('Menu Anterior', callback_data='menu_inicial'),
        row_width=2
    )
    return markup

# Função para criar o markup do menu TGA Financeiro
def create_menu_tga_financeiro():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton('Receber Imagem', callback_data='img'),
        types.InlineKeyboardButton('Receber PDF', callback_data='pdf'),
        types.InlineKeyboardButton('Receber Video', callback_data='mp4'),
        types.InlineKeyboardButton('Receber Audio', callback_data='mp3'),
        types.InlineKeyboardButton('Menu Anterior', callback_data='menu_inicial'),
        row_width=2
    )
    return markup

#Menus XD
# Função para criar o markup do menu XD
def create_menu_xd(): 
    markup = types.InlineKeyboardMarkup()
    markup.add(
            types.InlineKeyboardButton('XD PDV', callback_data='xd_pdv'),
            types.InlineKeyboardButton('XD Gestão', callback_data='xd_gestao'),
            types.InlineKeyboardButton('Menu Anterior', callback_data='menu_inicial'),
            row_width=2
        )
    return markup

# Menus SoftJava
# Função para criar o markup do menu SoftJava
def create_menu_sofjava(): 
    markup = types.InlineKeyboardMarkup()
    markup.add(
            types.InlineKeyboardButton('SoftJava PDV', callback_data='softjava_pdv'),
            types.InlineKeyboardButton('SoftJava Cloud', callback_data='softjava_cloud'),
            types.InlineKeyboardButton('Menu Anterior', callback_data='menu_inicial'),
            row_width=2
        )
    return markup



#     if call.data == 'tga_estoque':
#         bot.send_chat_action(chat_id=call.from_user.id, action='typing')
#         markup_opcoes = types.InlineKeyboardMarkup()
#         markup_opcoes.add(
#             types.InlineKeyboardButton('Teste Imagem', callback_data='img'),
#             types.InlineKeyboardButton('Teste PDF', callback_data='pdf'),
#             types.InlineKeyboardButton('Teste Video', callback_data='mp4'),
#             row_width=3
#         )
#         bot.send_message(chat_id=call.from_user.id, text='<b>Sr(a) {}</b>, escolha uma das opções abaixo:'.format(call.from_user.first_name), reply_markup=markup_opcoes)

#     if call.data == 'img': envio de imagem
#         bot.send_chat_action(chat_id=call.from_user.id, action='typing')
#         bot.send_photo(chat_id=call.from_user.id, photo=open('Tutoriais/Imagens/Teste.png', 'rb'),caption='Selecionado: Tutorial de tal coisa') 

bot.polling()