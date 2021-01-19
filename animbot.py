import requests
from lxml import html
import telebot
from telebot import types
 
api = 'Your telegram bot api'
bot = telebot.TeleBot(api)
 
#Your xpath from anime or manga website
#ANIME
path = "/html/body/div[3]/div/section[2]/div[2]/div[1]/a/@href"  # link anime
path2 = "/html/body/div[3]/section/div/div[2]/div[2]"  # info anime
path7 = "/html/body/div[3]/div/section[2]/div[2]/div[1]/a/div/div/div/div[1]/div/i" #Ratting anime
 
#MANGA
path3 = "/html/body/div[3]/div/section[1]/div[2]/div[1]/a/@href" #link manga
path4 = "/html/body/div[3]/div[4]/div[1]" # info manga
path5 = "/html/body/div[3]/section/div/div[2]/div[1]/div/ul" #Genre
path6 = "/html/body/div[3]/div[1]/div[2]/div[1]/div[2]" #manga Author
path8 = "/html/body/div[3]/div/section[1]/div[2]/div[1]/a/div/div/div/div[1]/div/i" #Ratting manga
 
@bot.message_handler(commands=['start', 'help', 'about'])
def send_welcome(message):
 markup = types.InlineKeyboardMarkup()
 itema = types.InlineKeyboardButton('Author', url = 'telegram.me/')
 markup.row(itema)
 bot.send_message(message.chat.id,'cari anime atau manga dengan ketik /search judul anime\n'+'hubungi admin di: @Username\n'+'Author : username\n', reply_markup=markup)
 
 
 markup.row(itema)
@bot.message_handler(commands=['search']) 
def echo_message(message):
    pesan = message.text
    bagi = pesan.split(' ',1)
    search = bagi[1]
    # untuk links
    url = ('Your anime website' + search)  # input url
    response = requests.get(url)
    
    if "Search Not Found" in response.text:
        bot.reply_to(message, "Judul Anime atau Manga Tidak Ditemukan!")
    elif "Search Manga Not Found" in response.text:
        #Link Anime
        byte_data = response.content
        source_code = html.fromstring(byte_data)
        tree = source_code.xpath(path)
        linkan = tree[0]
        rate = source_code.xpath(path7)
        ting = rate[0].text_content()
 
        #Desc Anime
        rest = requests.get(tree[0])
        bt = rest.content
        sc = html.fromstring(bt)
        tr = sc.xpath(path2)
        descan = tr[0].text_content()
        rw = sc.xpath(path5)
        gen = rw[0].text_content()
        #print("Link : \n"+linkan+"\nDescription : "+descan)
        bot.reply_to(message, "HASIL PENCARIAN ANIME \nLink : \n"+linkan+"\nGenre: \n"+gen+"\nRatting: "+ting+"\nDescription : "+descan)
    elif "Search Anime Not Found" in response.text:
        #Link Manga
        byte_data = response.content
        source_code = html.fromstring(byte_data)
        trii = source_code.xpath(path3)
        linkma = trii[0]
        mrate = source_code.xpath(path8)
        mting = mrate[0].text_content()
 
        #Desc Manga
        rs = requests.get(trii[0])
        by = rs.content
        sd = html.fromstring(by)
        treo = sd.xpath(path4)
        descma = treo[0].text_content()
        rw = sd.xpath(path5)
        gen = rw[0].text_content()
        up = sd.xpath(path6)
        date = up[0].text_content()
        #print("Link : \n"+linkma+"\nDescription : "+descma)
        bot.reply_to(message, "HASIL PENCARIAN MANGA \nLink : \n"+linkma+"\nGenre: \n"+gen+"\nRatting: "+mting+"\nDescription : "+descma+"\nAuthor: "+date)
    else:
        #Link Anime
        byte_data = response.content
        source_code = html.fromstring(byte_data)
        tree = source_code.xpath(path)
        linkan = tree[0]
        rate = source_code.xpath(path7)
        ting = rate[0].text_content()
 
        #Desc Anime
        rest = requests.get(tree[0])
        bt = rest.content
        sc = html.fromstring(bt)
        tr = sc.xpath(path2)
        descan = tr[0].text_content()
        rw = sc.xpath(path5)
        gen = rw[0].text_content()
        #print("Link : \n"+linkan+"\nDescription : "+descan)
        bot.reply_to(message, "HASIL PENCARIAN ANIME \nLink : \n"+linkan+"\nGenre: \n"+gen+"\nRatting: "+ting+"\nDescription : "+descan)
 
        #Link Manga
        trii = source_code.xpath(path3)
        linkma = trii[0]
        mrate = source_code.xpath(path8)
        mting = mrate[0].text_content()
 
        #Desc Manga
        rs = requests.get(trii[0])
        by = rs.content
        sd = html.fromstring(by)
        treo = sd.xpath(path4)
        descma = treo[0].text_content()
        rw = sc.xpath(path5)
        gen = rw[0].text_content()
        up = sd.xpath(path6)
        date = up[0].text_content()
        #print("Link : \n"+linkma+"\nDescription : "+descma)
        bot.reply_to(message, "HASIL PENCARIAN MANGA \nLink : \n"+linkma+"\nGenre: \n"+gen+"\nRatting: "+mting+"\nDescription : "+descma+"\nAuthor: "+date)
 
print('bot start running')
bot.polling()