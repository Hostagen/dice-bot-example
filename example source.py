import random

# in ext.commands.Bot()
# do stuff

@bot.command()
async def dice(ctx):
    random_num = random.randint(1, 100)
    print(random_num)

    str_num = str(random_num)
    keycap_nums = ["%s⃣" % num for num in str_num]
    embed = discord.Embed(description="🎲 %s" % "".join(keycap_nums))
    await ctx.send(embed=embed)

# in discord.Client()
# do stuff

@client.event
async def on_message(message):
    if message.content.startswith("!dice"):
      random_num = random.randint(1, 100)
      print(random_num)
      
      str_num = str(random_num)
      keycap_nums = ["%s⃣" % num for num in str_num]
      embed = discord.Embed(description="🎲 %s" % "".join(keycap_nums))
      await message.channel.send(embed=embed)
      
