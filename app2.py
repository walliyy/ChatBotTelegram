import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Leitura do arquivo de configuração
with open('config.ini', 'r') as f:
    config = f.read().splitlines()

# Criação do bot com o token do arquivo de configuração
bot = telebot.TeleBot(token=config[1], parse_mode='HTML')

# Dicionário para rastrear os menus
user_menus = {}

# Função para lidar com o comando /start ou o texto "start"
@bot.message_handler(commands=['start', 'Start'])
@bot.message_handler(func=lambda message: message.text.lower() == 'start')
def handle_start(message):
    markup = show_initial_menu()
    bot.send_message(chat_id=message.from_user.id, text='<b>Sr(a) {}</b>, seja bem vindo, escolha uma das opções abaixo:'.format(message.from_user.first_name), reply_markup=markup)
    show_initial_menu(message.chat.id)

# Função para exibir o menu inicial
def show_initial_menu(chat_id):
    user_menus[chat_id] = 'initial'  # Rastreia o menu atual do usuário

    # Criar os botões do menu inicial
    inline_keyboard = InlineKeyboardMarkup()
    menu1_button = InlineKeyboardButton("Menu 1", callback_data='menu1')
    menu2_button = InlineKeyboardButton("Menu 2", callback_data='menu2')
    inline_keyboard.row(menu1_button)
    inline_keyboard.row(menu2_button)

    bot.send_message(chat_id, "Selecione uma opção do menu:", reply_markup=inline_keyboard)

# Função para exibir o menu anterior
def show_previous_menu(chat_id):
    current_menu = user_menus.get(chat_id)
    if current_menu == 'menu1':
        show_initial_menu(chat_id)
    elif current_menu == 'menu2':
        show_initial_menu(chat_id)
    # Adicione mais blocos elif para cada menu adicional

# Função para lidar com os botões inline
@bot.callback_query_handler(func=lambda call: call.data in ['menu1', 'menu2'])
def menu_callback(call):
    chat_id = call.message.chat.id
    selected_menu = call.data
    user_menus[chat_id] = selected_menu  # Rastreia o menu atual do usuário

    if selected_menu == 'menu1':
        show_menu1(chat_id)
    elif selected_menu == 'menu2':
        show_menu2(chat_id)
    # Adicione mais blocos elif para cada menu adicional

# Função para exibir o Menu 1
def show_menu1(chat_id):
    user_menus[chat_id] = 'menu1'  # Rastreia o menu atual do usuário

    # Criar os botões do Menu 1
    inline_keyboard = InlineKeyboardMarkup()
    menu1_option1_button = InlineKeyboardButton("Opção 1", callback_data='menu1_option1')
    previous_menu_button = InlineKeyboardButton("Menu Anterior", callback_data='previous_menu')
    inline_keyboard.row(menu1_option1_button)
    inline_keyboard.row(previous_menu_button)

    bot.send_message(chat_id, "Selecione uma opção do Menu 1:", reply_markup=inline_keyboard)

# Função para exibir o Menu 2
def show_menu2(chat_id):
    user_menus[chat_id] = 'menu2'  # Rastreia o menu atual do usuário

    # Criar os botões do Menu 2
    inline_keyboard = InlineKeyboardMarkup()
    menu2_option1_button = InlineKeyboardButton("Opção 1", callback_data='menu2_option1')
    previous_menu_button = InlineKeyboardButton("Menu Anterior", callback_data='previous_menu')
    inline_keyboard.row(menu2_option1_button)
    inline_keyboard.row(previous_menu_button)

    bot.send_message(chat_id, "Selecione uma opção do Menu 2:",reply_markup=inline_keyboard)

# Função para lidar com o botão "Menu Anterior"
@bot.callback_query_handler(func=lambda call: call.data == 'previous_menu')
def previous_menu_callback(call):
    chat_id = call.message.chat.id
    show_previous_menu(chat_id)

# Iniciar o bot
bot.polling()






# # Handler para o comando /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = create_menu_markup()
#     bot.send_message(chat_id=message.from_user.id, text='<b>Sr(a) {}</b>, seja bem vindo, escolha uma das opções abaixo:'.format(message.from_user.first_name), reply_markup=markup)

# # Função para criar o markup do menu
# def create_menu_markup():
#     markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     item1 = types.KeyboardButton('💻 Suporte TGA')
#     item2 = types.KeyboardButton('💻 Suporte XD')
#     item3 = types.KeyboardButton('💻 Suporte SoftJava')
#     # item4 = types.KeyboardButton('Acesse: TecnoPro Sistemas', url='http://www.tecnopro.inf.br/site/')
#     markup.add(item1, item2, item3)
#     return markup

# # Função para criar o menu TGA
# def create_menu_tga():
#     markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     item1 = types.KeyboardButton('TGA Estoque')
#     item2 = types.KeyboardButton('TGA Financeiro')
#     back_button = types.KeyboardButton('Menu anterior')
#     markup.add(item1, item2, back_button)
#     return markup

# # Handler para a opção 1
# @bot.message_handler(func=lambda message: message.text == '💻 Suporte TGA')
# def option1(message):
#     markup = create_menu_tga()
#     bot.send_message(message.chat.id, 'Você escolheu <b>Suporte TGA</b>', reply_markup=markup)
    
# # Handler para a opção 2
# @bot.message_handler(func=lambda message: message.text == 'Opção 2')
# def option2(message):
#     bot.send_message(message.chat.id, 'Você escolheu a Opção 2')

# # Handler para voltar ao menu anterior
# @bot.message_handler(func=lambda message: message.text == 'Menu anterior')
# def back_to_menu(message):
#     markup = create_menu_markup()
#     bot.send_message(message.chat.id, 'Voltando ao menu anterior:', reply_markup=markup)

# Inicie o bot
# bot.polling()
