import keep_alive

keep_alive.keep_alive()

# bot.py
import discord
import os
import re

from discord import channel
from discord.ext import commands
from random import randint, seed
from random import random
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
import json
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']
CHANNEL = os.environ['DISCORD_CHANNEL']
ALLQ = os.environ['ALL']
ANDYOUANDITEXT = os.environ['ANDYOU']
client = discord.Client()

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


@client.event
async def on_ready():
    # code for seeing if it is on the right server
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    await client.change_presence(activity=discord.Game('What a lovely day to draw a pyramid!'))
    print(f'{CHANNEL}')
    

    
banned_words={"stfu","jail","wtf","vvhore", "sthu" ,"4r5e", "5h1t", "5hit", "a55", "anal", "anus", "ar5e", "arrse", "arse", "ass", "ass-fucker", "asses", "assfucker", "assfukka", "asshole", "assholes", "asswhole", "a_s_s", "b!tch", "b00bs", "b17ch", "b1tch", "ballbag", "balls", "ballsack", "bastard", "beastial", "beastiality", "bellend", "bestial", "bestiality", "bi+ch", "biatch", "bitch", "bitcher", "bitchers", "bitches", "bitchin", "bitching", "bloody", "blow job", "blowjob", "blowjobs", "boiolas", "bollock", "bollok", "boner", "boob", "boobs", "booobs", "boooobs", "booooobs", "booooooobs", "breasts", "buceta", "bugger", "bum", "bunny fucker", "butt", "butthole", "buttmuch", "buttplug", "c0ck", "c0cksucker", "carpet muncher", "cawk", "chink", "cipa", "cl1t", "clit", "clitoris", "clits", "cnut", "cock", "cock-sucker", "cockface", "cockhead", "cockmunch", "cockmuncher", "cocks", "cocksuck", "cocksucked", "cocksucker", "cocksucking", "cocksucks", "cocksuka", "cocksukka", "cok", "cokmuncher", "coksucka", "coon", "cox", "crap", "cum", "cummer", "cumming", "cums", "cumshot", "cunilingus", "cunillingus", "cunnilingus", "cunt", "cuntlick", "cuntlicker", "cuntlicking", "cunts", "cyalis", "cyberfuc", "cyberfuck", "cyberfucked", "cyberfucker", "cyberfuckers", "cyberfucking", "d1ck", "damn", "dick", "dickhead", "dildo", "dildos", "dink", "dinks", "dirsa", "dlck", "dog-fucker", "doggin", "dogging", "donkeyribber", "doosh", "duche", "dyke", "ejaculate", "ejaculated", "ejaculates", "ejaculating", "ejaculatings", "ejaculation", "ejakulate", "f u c k", "f u c k e r", "f4nny", "fag", "fagging", "faggitt", "faggot", "faggs", "fagot", "fagots", "fags", "fanny", "fannyflaps", "fannyfucker", "fanyy", "fatass", "fcuk", "fcuker", "fcuking", "feck", "fecker", "felching", "fellate", "fellatio", "fingerfuck", "fingerfucked", "fingerfucker", "fingerfuckers", "fingerfucking", "fingerfucks", "fistfuck", "fistfucked", "fistfucker", "fistfuckers", "fistfucking", "fistfuckings", "fistfucks", "flange", "fook", "fooker", "fuck", "fucka", "fucked", "fucker", "fuckers", "fuckhead", "fuckheads", "fuckin", "fucking", "fuckings", "fuckingshitmotherfucker", "fuckme", "fucks", "fuckwhit", "fuckwit", "fudge packer", "fudgepacker", "fuk", "fuker", "fukker", "fukkin", "fuks", "fukwhit", "fukwit", "fux", "fux0r", "f_u_c_k", "gangbang", "gangbanged", "gangbangs", "gaylord", "gaysex", "goatse", "God", "god-dam", "god-damned", "goddamn", "goddamned", "hardcoresex", "hell", "heshe", "hoar", "hoare", "hoer", "homo", "hore", "horniest", "horny", "hotsex", "jack-off", "jackoff", "jap", "jerk-off", "jism", "jiz", "jizm", "jizz", "kawk", "knob", "knobead", "knobed", "knobend", "knobhead", "knobjocky", "knobjokey", "kock", "kondum", "kondums", "kum", "kummer", "kumming", "kums", "kunilingus", "l3i+ch", "l3itch", "labia", "lust", "lusting", "m0f0", "m0fo", "m45terbate", "ma5terb8", "ma5terbate", "masochist", "master-bate", "masterb8", "masterbat*", "masterbat3", "masterbate", "masterbation", "masterbations", "masturbate", "mo-fo", "mof0", "mofo", "mothafuck", "mothafucka", "mothafuckas", "mothafuckaz", "mothafucked", "mothafucker", "mothafuckers", "mothafuckin", "mothafucking", "mothafuckings", "mothafucks", "mother fucker", "motherfuck", "motherfucked", "motherfucker", "motherfuckers", "motherfuckin", "motherfucking", "motherfuckings", "motherfuckka", "motherfucks", "muff", "mutha", "muthafecker", "muthafuckker", "muther", "mutherfucker", "n1gga", "n1gger", "nazi", "nigg3r", "nigg4h", "nigga", "niggah", "niggas", "niggaz", "nigger", "niggers", "nob", "nob jokey", "nobhead", "nobjocky", "nobjokey", "numbnuts", "nutsack", "orgasim", "orgasims", "orgasm", "orgasms", "p0rn", "pawn", "pecker", "penis", "penisfucker", "phonesex", "phuck", "phuk", "phuked", "phuking", "phukked", "phukking", "phuks", "phuq", "pigfucker", "pimpis", "piss", "pissed", "pisser", "pissers", "pisses", "pissflaps", "pissin", "pissing", "pissoff", "poop", "porn", "porno", "pornography", "pornos", "prick", "pricks", "pron", "pube", "pusse", "pussi", "pussies", "pussy", "pussys", "rectum", "retard", "rimjaw", "rimming", "s hit", "s.o.b.", "sadist", "schlong", "screwing", "scroat", "scrote", "scrotum", "semen", "sex", "sh!+", "sh!t", "sh1t", "shag", "shagger", "shaggin", "shagging", "shemale", "shi+", "shit", "shitdick", "shite", "shited", "shitey", "shitfuck", "shitfull", "shithead", "shiting", "shitings", "shits", "shitted", "shitter", "shitters", "shitting", "shittings", "shitty", "skank", "slut", "sluts", "smegma", "smut", "snatch", "son-of-a-bitch", "spac", "spunk", "s_h_i_t", "t1tt1e5", "t1tties", "teets", "teez", "testical", "testicle", "tit", "titfuck", "tits", "titt", "tittie5", "tittiefucker", "titties", "tittyfuck", "tittywank", "titwank", "tosser", "turd", "tw4t", "twat", "twathead", "twatty", "twunt", "twunter", "v14gra", "v1gra", "vagina", "viagra", "vulva", "w00se", "wang", "wank", "wanker", "wanky", "whoar", "whore", "willies", "willy", "xrated", "xxx"}

@client.event
async def on_message(message):
    if message.author != client.user:
        await word_check(message)
        await pyramid(message)
        await commands(message)
        if int(message.author.id) == int(ALLQ): 
            if "tall" in message.content or "Tall" in message.content:
                 await message.reply("short.")
    if client.user.mentioned_in(message) and message.author != client.user:
        await message.reply("kk")


async def word_check(message):
    for word in banned_words:
        if findWholeWord(word)(message.content):
            await message.reply("no u")
    f = open('responses.json',)
  
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
  
    # Iterating through the json
    # list
    for i in data:
        if i in message.content.lower():
            await message.reply(data[i])
    f.close()
#    if "Marquez" in message.content or "marquez" in message.content:
 #       await message.reply("*Marcus")
    
async def commands(message):
    if message.content.startswith("$google"):
        for j in search(remove_prefix(message.content,"$google"), tld="co.in", num=1, stop=1, pause=2):
            await message.reply(j)
    if message.content.startswith("$magic8"):
        q = ""
        v = randint(0,9)
        if v == 0:
                q = "No"
        if v == 1:
                q = "Yes"
        if v == 2:
                q = "Possibly"
        if v == 3:
                q = "As likely as the moon touching the Earth"
        if v == 4:
                q = "Try again later"
        if v == 5:
                q = "hmmmmmmmm"
        if v == 6:
                q = "Ask a 6 sided dice"
        if v == 7:
                q = "The opposite of the next result is the answer you seek"
        if v == 8:
                q = "I'm not going to answer that"
        if v == 9: 
                q = "Yes AND no"
        await message.reply(q)
    if message.content.startswith("$addtrigger "):
        f = open('responses.json',)
  
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
  
        # Iterating through the json
        # list
        for i in data:
            if i in message.content.lower():
                message.reply("this phrase is already used")
                return
        if remove_prefix(message.content,"$addtrigger ").partition(":")[1]:
            data[remove_prefix(message.content,"$addtrigger ").partition(":")[0]] = remove_prefix(message.content,"$addtrigger ").partition(":")[2]
        f.close()
        with open('responses.json', 'w') as outfile:
            json.dump(data, outfile, indent = 6)
        outfile.close()
    if message.content.startswith("$removetrigger "):
        f = open('responses.json',)
  
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
  
        # Iterating through the json
        # list
        for i in data:
            if i in message.content.lower():
                if remove_prefix(message.content,"$removetrigger ") == i:
                    data.pop(i)
                    await message.reply("the phrase has been removed")
                    f.close()
                    with open('responses.json', 'w') as outfile:
                        json.dump(data, outfile, indent = 6)
                    outfile.close()
                    return
#bot = commands.Bot(command_prefix='$')
#@bot.command()s
#async def ping(ctx, query):
#    for j in search(query, tld="co.in", num=1, stop=10, pause=2):
#        await ctx.channel.send(j)




async def pyramid(message):
    if message.content.isdigit():
            b = int(message.content)
            q = "```"
            for i in range(0, b):
                for z in range(0,b-i):
                    q += " "
                for j in range(0,i+1):
                    q += "* "
                q += "\n"
            q += "```"
            if b < 501:
                await recursive_send(q, message)
async def recursive_send(q, message):
    channel = client.get_channel(int(CHANNEL))
    if len(q) > 2000:
        await recursive_send(q[:len(q)//2] + "```", message)
        await recursive_send("```" + q[len(q)//2:], message)
    else:
        await message.reply(q)

#client.run(TOKEN)
client.run(TOKEN)

