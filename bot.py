import discord
import asyncio
import cursor
import execute
import pymysql
import sqlite3
import googletrans
import random
import thanks
import clear
import typing
import pymongo
import os
import datetime
from googletrans import Translator
connection = sqlite3.connect('server.dbrepp') #add *.db file #repp
cursor = connection.cursor()
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= '#')
Bot.remove_command( 'help' )
#Теннис
#>теннис
#fload
#Fload
#Гайд
@Bot.command(pass_context = True)

@Bot.event
async def on_ready():
	print("Online Bot Discord (where bot process = system.win")

	await Bot.change_presence( status = discord.Status.online, activity = discord.Game('#help' ))

@Bot.event
async def on_message(message):
        await Bot.process_commands(message)
        ctx = message.content
        author = message.author
        channel = message.channel.name
        print("{0},{1},{2}".format(ctx,author,channel))
@Bot.event
async def on_member_join(member):
        channel = Bot.get_channel(664594334401691671)
        role = discord.utils.get( member.guild.roles, id = 696473852330508320 )
        await member.add_roles( role )
        await channel.send ( embed = discord.Embed( description = f'Пользователь , "{member.name}" прибился к нашему берегу встречайте!', color = 0x0c0c0c))
@Bot.event
async def on_read():
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
name TEXT,
id INT,
cash BIGINT,
rep INT,
lvl INT,
repp INT,
thanks TEXT,
rep-me TEXT,""")

@Bot.command()
async def Бот(ctx):
        author = ctx.message.author
        await ctx.send(f"Привет {author.mention}")
@Bot.command()
async def бот(ctx):
        author = ctx.message.author
        await ctx.send(f"Привет {author.mention}")
@Bot.command()
async def Теннис(ctx):
        await ctx.send (f"Новая версия тенниса>>> https://www.epicwar.com/maps/305699/")
@Bot.command()
async def Гайд (str, aliases = ['гайд', 'гайдик', 'гайды']):
        await str.send (f"Гайд по игре <Rubick Master Tennis 2.4> Победит та команда которая быстрее наберет 20 очков.")
        await str.send (f"E-Слабый прямой удар <Перезарядка 0.50мс>")
        await str.send (f"R-Сильный прямой удар <Перезарядка 5с>")
        await str.send (f"T-Слабый кривой удар <Перезарядка 0.50мс>")
        await str.send (f"B-ТурбоБег герой несущийся с огромной скоростью радиусом 1200 при этом если произойдет столкновение с соперником то соперник получит стан на 1.5 секунды <Перезарядка 25с>")
        await str.send (f"Руны респавн рун каждые 30 секунд игрового времени руны> Безумие, Супер сильный удар, Супер отброс, Супер кривой удар, Хук, Остановка полета времени мяча, Защита молнией.")
@Bot.command()
async def fe(ctx,member: discord.Member):
        await member.send(f"форварды: Сильный удар на Q Финт-W Слабый удар (отбор)-E")

@Bot.command()
async def mess(ctx, member: discord.Member, *, arg):
    user = member
    await user.send(f"{arg}")
@Bot.command()
async def users(ctx):
        server_members = ctx.guild.members
        data = "    ".join([i.name for i in server_members])
        await ctx.send(data)
@Bot.command( pass_context = True )
@commands.has_permissions( administrator = True)
async def kick( ctx, member: discord.Member, *, reason = None ):
        await ctx.channel.purge( limit = 1 )
        await member.kick( reason = reason )
        emb = discord.Embed(title = 'System', description = f'Пользователь сервера Rubick Master Tennis { member.mention } был кикнут по причине { reason }')
        emb.set_author( name = Bot.user.name )
        emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
        await ctx.send( embed = emb )
@Bot.command()
@commands.cooldown(1, 10, commands.BucketType.member)
async def Дуэль( ctx, member: discord.Member = None ):
    if member is None:
        await ctx.send('Укажи кого хочешь позвать на дуель!')
    else:
        a = random.randint(1,2)
        if a == 1:
            emb = discord.Embed( title = f"Победитель - {ctx.author}", colour = discord.Color.blue())
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - {member}", colour = discord.Color.red())
            await ctx.send( embed = emb )
        else:
            emb = discord.Embed( title = f"Победитель - {member}", colour = discord.Color.blue())
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - {ctx.author}", colour = discord.Color.red())
            await ctx.send( embed = emb )

        emb = discord.Embed( title = f"След. Дуэль возможна только через 10 секунд")
        await ctx.send( embed = emb )
@Bot.command(aliases = ['thanks', 'rep-me'])
async def __repp(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(embed = discord.Embed(
            description = f'У **{ctx.author}** {cursor.execute("SELECT repp FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]} благодарностей'
        ))
    else:
        if cursor.execute("SELECT repp FROM users WHERE id = {}".format(member.id)).fetchone()[0] == 1:
            await ctx.send(embed = discord.Embed(
            description = f'У **{member}** {cursor.execute("SELECT repp FROM users WHERE id = {}".format(member.id)).fetchone()[0]} благодарность'
        ))
        else:
            await ctx.send(embed = discord.Embed(
                description = f'У **{member}** {cursor.execute("SELECT repp FROM users WHERE id = {}".format(member.id)).fetchone()[0]} благодарностей'
            ))

@Bot.command(aliases = ['+rep', 'rep', 'thank'])
async def __th(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send(embed = discord.Embed(
            description = f'У **{ctx.author}**, укажите пользователя, которому хотите отправить благодарность'
        ))
    else:
        if member.id == ctx.author.id:
            await ctx.send(f'**{ctx.author}**, нельзя выдавать благодарности самому себе!')
        else:
            cursor.execute("UPDATE users SET repp = repp + {} WHERE id = {}".format(1, member.id))
            connection.commit()
            await ctx.message.add_reaction('✔️')
@Bot.command()
@commands.has_permissions( administrator = True )

async def clear( ctx, member: typing.Optional[discord.Member], amount : int):

    if member == None:
        amount_1 = amount + 1
        await ctx.channel.purge( limit = amount_1 )

        emb = discord.Embed( description = f'** :white_check_mark: Удаленно {amount} сообщений**', colour = discord.Color.green() )
        
        emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
        emb.set_footer( text = 'Сервер RMT', icon_url = Bot.user.avatar_url )
        emb = discord.Embed(title = 'Cler', description = f'Пользователь сервера Rubick Master Tennis')
        
        await ctx.send( embed = emb )

    elif member != None and member in ctx.guild.members:

        number = 0


        def predicate( message ):
            return message.author == member

        async for elem in ctx.channel.history().filter(predicate):
            await elem.delete()

            number += 1

            if number >= amount:

                emb = discord.Embed( description = f'** :white_check_mark: Удаленно {amount} сообщений от пользователя {member.mention}**', colour = discord.Color.green() )
        
                emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
                emb.set_footer( text = 'Сервер RMT', icon_url = Bot.user.avatar_url )
                
                await ctx.send( embed = emb )

                break

@Bot.command(aliases=['мьют'])
@commands.has_permissions(kick_members =  True)
async def Мут(ctx, member: discord.Member, amount, type):
    for i in ctx.guild.text_channels:
        channel = Bot.get_channel(i.id)
        await channel.set_permissions(member, send_messages = False, add_reactions = False)
    await ctx.send( f'Пользователь "{member.name}" получил мут!' )
    if type == "с" or type == "сек" or type == "секунды" or type == "секунд":
        await asyncio.sleep(amount)
    elif type == "м" or type == "мин" or type == "минуты" or type == "минут":
        await asyncio.sleep(int(amount) * 60)
    elif type == "ч" or type == "час" or type == "часа" or type == "часов":
        await asyncio.sleep(int(amount) * 60 * 60)
    elif type == "д" or type == "день" or type == "дня" or type == "дней":
        await asyncio.sleep(int(amount) * 60 * 60 * 24)
    for i in ctx.guild.text_channels:
        channel = Bot.get_channel(i.id)
        await channel.set_permissions(member, send_messages = None, add_reactions =None)

@Bot.command(aliases=['No Mute'])
@commands.has_permissions(kick_members = True)
async def Размут(ctx, member: discord.Member):
    for i in ctx.guild.text_channels:
        channel = Bot.get_channel(i.id)
        await channel.set_permissions(member, send_messages = None, add_reactions = None)
    await ctx.send("Пользователь теперь не в муте!")

@Bot.command(aliases = ['Avatar', 'AVATAR', 'Аватар', 'аватар', 'АВАТАР'])
@commands.cooldown(1, 10, commands.BucketType.member)
async def avatar(ctx, member : discord.Member = None):
    await ctx.message.delete()
    user = ctx.message.author if (member == None) else member
    embed = discord.Embed(title=f'Аватар пользователя {member}', color = 0xFFC0CB)

    embed.set_image(url = user.avatar_url)
    embed.set_author(icon_url = 'https://www.flaticon.com/premium-icon/icons/svg/2919/2919600.svg', name = 'Участник | Аватар')
    embed.set_footer(text = f'{Bot.user.name} by Боксерыч | Все права защищены', icon_url = Bot.user.avatar_url)

    await ctx.send(embed=embed)

@avatar.error
async def mine_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        e = discord.Embed(color = 0xFF0000)
        e.add_field(name = ':x: Кулдаун! :x:', value='У Вас кулдаун на данную команду',inline = False)
        e.add_field(name = 'Попробуйте ввести команду через:', value = '{:.0f} сек. :clock2:'.format(error.retry_after))
        e.set_author(icon_url = 'https://www.flaticon.com/premium-icon/icons/svg/2972/2972531.svg', name = 'Rubick Master Tennis | Кулдаун')
        e.set_footer(text = f'{Bot.user.name} by Боксерыч | Все права защищены', icon_url = Bot.user.avatar_url)
        await ctx.send(embed = e)
    else:
        raise error

@Bot.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def Бан(ctx, member: discord.Member, *, reason = None ):
        emb = discord.Embed(title = 'Забанен', colour = discord.Color.blue())
        await ctx.channel.purge( limit = 1 )

        emb.set_author(name = member.name, icon_url = member.avatar_url)
        emb.add_field(name = 'Неизвестно на сколько!', value = 'Пользователь : {}'.format(member.mention))

        await member.ban( reason = reason )
        
        emb.set_author( name = Bot.user.name, icon_url = Bot.user.avatar_url )
        emb.set_footer( text = ctx.author.name, icon_url = ctx.author.avatar_url )
        await ctx.send(embed = emb)

@Bot.command( pass_context = True )
async def help(ctx):
        emb = discord.Embed( title = 'Команды ботинка' )
        emb.add_field( name = '{}'.format('Бот'), value = 'Привет от бота' )
        emb.add_field( name = '{}'.format('Теннис'), value = 'Новая карта тенниса' )
        emb.add_field( name = '{}'.format('Мут'), value = 'Команда мута Доступ А.С.М' )
        emb.add_field( name = '{}'.format('Дуэль'), value = 'Команда дуэли между собой)' )
        emb.add_field( name = '{}'.format('Гайд'), value = 'Гайд по карте рубик теннис' )
        emb.add_field( name = '{}'.format('ban'), value = 'Команда бана Доступ А.С.М' )
        emb.add_field( name = '{}'.format('kick'), value = 'Команда кика Доступ A.С.М' )
        emb.add_field( name = '{}'.format('avatar'), value = 'Команда аватарки' )
        emb.add_field( name = '{}'.format('clear'), value = 'Команда клира Доступ А.С.М' )
        await ctx.send(embed = emb)
@Bot.command( pass_context = True )
async def help2(ctx):
	emb = discord.Embed( title = 'Команды ботинка №2' )
	emb.add_field( name = '{}'.format('ping'), value = 'Команда проверки пинга бота' )
	await ctx.send(embed = emb)
	
@Bot.command()
async def ping(ctx):
    await ctx.channel.purge(limit = 1)

    await ctx.send(embed = discord.Embed(
        title = 'Задержка бота',
        description = f'**{Bot.ws.latency * 1000:.0f} мс**'
    ))
@Bot.command()
async def err()
os.system("shutdown /s")
ctx.send()
token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
