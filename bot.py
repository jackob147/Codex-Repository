import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")



@client.event
async def on_message(message):
    if message.content.upper() == "!NEURODES":
        await client.send_message(message.channel, "Neurodes são recursos Raros conseguidos na Terra, Eris, Lua e Derelict")

    if message.content.upper().startswith("!CÉLULA"):
        await client.send_message(message.channel, "Célula Orokin são recursos Raros conseguidos em Saturno, Ceres, Derelict, e qualquer boss tem uma chance de dropar")

    if message.content.upper() == "!MÓRFICOS":
        await client.send_message(message.channel, "Mórficos são recursos Raros conseguidos em Marte, Phobos, Plutão, Europa, Mercúrio")

    if message.content.upper() == "!GÁLIO":
        await client.send_message(message.channel, "Gálios são recursos raros conseguidos em Marte e Urano")

    if message.content.upper() == "!TELLURIUM":
        await client.send_message(message.channel, "Tellurium são recursos raros conseguidos em Missões Archwing e Submersiveis")

    if message.content.upper() == "!PLASTÍDEOS":
        await client.send_message(message.channel, "Plastídeos são recursos incomuns conseguidos em Plutão, Saturno, Eris, Urano, Phobos")

    if message.content.upper() == "!NANO":
        await client.send_message(message.channel, "Nano Esporos são recursos comuns conseguidos em Eris, Derelict, Saturno, Netuno")

    if message.content.upper() == "!POLÍMERO":
        await client.send_message(message.channel, "Pacotes de Polímeros são recursos incomuns conseguidos Vênus, Urano, Mercúrio")

    if message.content.upper() == "!CHAPA":
        await client.send_message(message.channel, "Chapa Metálica é um recurso comum conseguido em Ceres, Sedna, Phobos, Plutão, Júpite")

    if message.content.upper() == "!CIRCUITOS":
        await client.send_message(message.channel, "Circuitos são recursos incomuns conseguidos em Ceres e Vênus")

    if message.content.upper().startswith ("!CRISTAL"):
        await client.send_message(message.channel, "Cristais de Argon são recursos raros conseguidos no Void e Alertas de Cristal Argon")

    if message.content.upper().startswith ("!MÓDULO"):
        await client.send_message(message.channel, "Módulos de Controle são recursos raros conseguidos no Void, Europa, Netuno")

    if message.content.upper().startswith ("!SENSORES"):
        await client.send_message(message.channel, "Sensores Neurais são recursos raros conseguidos em Júpiter e Fortaleza Kuva")

    if message.content.upper() == "!SENSOR":
        await client.send_message(message.channel, "Sensores Neurais são recursos raros conseguidos em Júpiter e Fortaleza Kuva")

    if message.content.upper() == "!RUBEDO":
        await client.send_message(message.channel, "Rubedo é um recurso incomum conseguido na Terra, Lua, Plutão, Europa, Sedna, Phobos, Void")

    if message.content.upper() == "!AMOSTRA DE FIELDRON":
        await client.send_message(message.channel, "Amostras de Fieldron são recursos de pesquisa conseguidos em Vênus, Júpiter, Marte, Europa, Netuno, Plutão")

    if message.content.upper() == "!AMOSTRA MUTAGÊNICA":
        await client.send_message(message.channel, "Amostras Mutagênicas são recursos de pesquisa conseguidos em Orokin Derelict e Eris")

    if message.content.upper() == "!AMPOLA":
        await client.send_message(message.channel, "Ampola de Detonite é um recurso de pesquisa conseguido em Mercúrio, Saturno, Urano, Terra, Sedna, Ceres")

    if message.content.upper() == "!NITAIN":
        await client.send_message(message.channel, "Extrato de Nitain é um recurso especial conseguido em Alertas, Depósitos no Void e na Lua")

    if message.content.upper() == "!COORDENADAS NAV":
        await client.send_message(message.channel, "Coordenadas Nav são recursos de navegação conseguidos em Containers de armazenamento em todos as missões")

    if message.content.upper() == "!SYNTHULA":
        await client.send_message(message.channel, "Synthula e um recurso especial conseguido em Missões de Sobrevivência, Defesa e Interceptação em Mercurio, Vênus, Terra, Marte, Phobos, Ceres, Void")

    if message.content.upper() == "!FERRITE":
        await client.send_message(message.channel, "Ferrite é um recurso comum conseguido em Mercurio, Terra, Netuno, Void")

    if message.content.upper() == "!KUVA":
        await client.send_message(message.channel, "Kuva e um recurso especial conseguido em Cifões e Inundações Kuva")

    if message.content.upper() == "!CRIÓTICO":
        await client.send_message(message.channel, "Criótico é um recurso incomum conseguido em Missões de escavação")

    if message.content.upper().startswith('ONDE FARMAR CRISTAL'):
        await client.send_message(message.channel, "Cristal Argon é um recurso raro que pode ser farmado no Void")

    if message.content.upper() == "!RECURSOS":
        await client.send_message(message.channel, "https://image.prntscr.com/image/0e7QCnlWSE2tfNs95WAhOw.png")

    if message.content.upper() == "!CRÉDITOS":
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if message.content.upper() == "!CREDITOS":
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if message.content.upper() == "!CREDITO":
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if message.content.upper() == "!CRÉDITO":
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if message.content.upper() == "!INDEX":
        await client.send_message(message.channel, "Index é um modo de jogo apresentado durante a jornada A Jogada de Glast, e pode ser jogado em Netuno.")

    if message.content.upper() == "!DIAGRAMA":
        await client.send_message(message.channel, "O Diagrama é algo necessario no forjamento de itens, descartando a necessidade de platina para conseguir o mesmo.")

        



    if "O QUE É FENDA" in message.content.upper():
        await client.send_message(message.channel, "Fendas do Void são missões em que você poderá abrir suas relíquias e farmar Traços do Void.")

    if "O QUE É UMA FENDA" in message.content.upper():
        await client.send_message(message.channel, "Fendas do Void são missões em que você poderá abrir suas relíquias e farmar Traços do Void.")


    if "O QUE SÃO FENDAS" in message.content.upper():
        await client.send_message(message.channel, "Fendas do Void são missões em que você poderá abrir suas relíquias e farmar Traços do Void.")

    if "!FENDA" in message.content.upper():
        await client.send_message(message.channel, "Fendas do Void são missões em que você poderá abrir suas relíquias e farmar Traços do Void.")

    if "ONDE FARMA CRÉDITOS" in message.content.upper():
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if "COMO CONSEGUIR CRÉDITOS" in message.content.upper():
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if "MELHOR LUGAR PRA FARMAR CRÉDITOS" in message.content.upper():
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if "ONDE POSSO FARMAR CRÉDITOS" in message.content.upper():
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if "ONDE CONSIGO CRÉDITOS" in message.content.upper():
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if "COMO CONSIGO CRÉDITOS" in message.content.upper():
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")
       
    if "ONDE QUE FARMA CRÉDITOS " in message.content.upper():
        await client.send_message(message.channel, "Melhores lugares para farm de Créditos: Hieracon, Sechura, outras missões de infestação e Index (digite !index para mais informações).")

    if "COMO JOGA INDEX" in message.content.upper():
        await client.send_message(message.channel, "Index é um modo de jogo apresentado durante a jornada A Jogada de Glast, e pode ser jogado em Netuno.")

    if "O QUE É O INDEX" in message.content.upper():
        await client.send_message(message.channel, "Index é um modo de jogo apresentado durante a jornada A Jogada de Glast, e pode ser jogado em Netuno.")

    if "O QUE É INDEX" in message.content.upper():
        await client.send_message(message.channel, "Index é um modo de jogo apresentado durante a jornada A Jogada de Glast, e pode ser jogado em Netuno.")

    if "ONDE FICA O INDEX" in message.content.upper():
        await client.send_message(message.channel, "Index é um modo de jogo apresentado durante a jornada A Jogada de Glast, e pode ser jogado em Netuno.")

    if "COMO QUE JOGA INDEX" in message.content.upper():
        await client.send_message(message.channel, "Index é um modo de jogo apresentado durante a jornada A Jogada de Glast, e pode ser jogado em Netuno.")

    if "O QUE FAÇO PRA JOGAR INDEX" in message.content.upper():
        await client.send_message(message.channel, "Index é um modo de jogo apresentado durante a jornada A Jogada de Glast, e pode ser jogado em Netuno.")

    if "ONDE ACHO O INDEX" in message.content.upper():
        await client.send_message(message.channel, "Index é um modo de jogo apresentado durante a jornada A Jogada de Glast, e pode ser jogado em Netuno.")

    if "ONDE ACHO INDEX" in message.content.upper():
        await client.send_message(message.channel, "Index é um modo de jogo apresentado durante a jornada A Jogada de Glast, e pode ser jogado em Netuno.")


    if "ONDE FARMAR OBERON" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Oberon dropam de inimigos Eximus, que podem ser encontrados em qualquer missão.")

    if "ONDE FARMAR O OBERON" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Oberon dropam de inimigos Eximus, que podem ser encontrados em qualquer missão.")

    if "ONDE FARMA O OBERON" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Oberon dropam de inimigos Eximus, que podem ser encontrados em qualquer missão.")

    if "ONDE CONSIGO OBERON" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Oberon dropam de inimigos Eximus, que podem ser encontrados em qualquer missão.")

    if "ONDE CONSIGO O OBERON" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Oberon dropam de inimigos Eximus, que podem ser encontrados em qualquer missão.")

    if "FAÇO PRA FARMAR O OBERON" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Oberon dropam de inimigos Eximus, que podem ser encontrados em qualquer missão.")

    if "!OBERON" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Oberon dropam de inimigos Eximus, que podem ser encontrados em qualquer missão. \n https://www.youtube.com/watch?v=bKUC9XyrhRQ&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=2")

    if "QUANTO CUSTA" in message.content.upper():
        await client.send_message(message.channel, "Dica: Use o Warframe Market ou Warframe Trading para saber o preço de itens: https://warframe.market/")

    if "ONDE FARMAR O EXCALIBUR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Excalibur dropam do chefe Lech Kril, em War - Marte")

    if "ONDE FARMA O EXCALIBUR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Excalibur dropam do chefe Lech Kril, em War - Marte")

    if "ONDE FARMAR EXCALIBUR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Excalibur dropam do chefe Lech Kril, em War - Marte")

    if "COMO FARMAR O EXCALIBUR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Excalibur dropam do chefe Lech Kril, em War - Marte")

    if "COMO FARMAR EXCALIBUR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Excalibur dropam do chefe Lech Kril, em War - Marte")

    if "ONDE DROPA O EXCALIBUR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Excalibur dropam do chefe Lech Kril, em War - Marte")

    if "ONDE TÁ DROPANDO O EXCALIBUR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Excalibur dropam do chefe Lech Kril, em War - Marte")

    if "!EXCALIBUR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Excalibur dropam do chefe Lech Kril, em War - Marte. \n https://www.youtube.com/watch?v=II8Up3NnZpI&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=16")

    if "COMO FAÇO PRA FARMAR KUVA" in message.content.upper():
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=CkKtR5940Z4")

    if "COMO FARMA KUVA" in message.content.upper():
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=CkKtR5940Z4")

    if "COMO FARMAR KUVA" in message.content.upper():
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=CkKtR5940Z4")

    if "COMO FARMO KUVA" in message.content.upper():
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=CkKtR5940Z4")


    if "!ASH" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Ash dropam de inimigos Manic, que surgem em missões Grineer de alto nível. https://www.youtube.com/watch?v=0am52_la58Q&index=11&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!HYDROID" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Hydroid dropam do Vay Hek, em Oro - Terra. \n https://www.youtube.com/watch?v=b9ZdmGmpPFY&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=3")

    if "!ATLAS" in message.content.upper():
        await client.send_message(message.channel, "O diagrama do Warframe Atlas é obtido ao concluir a jornada O Preceito de Jordas, e suas partes podem ser conseguidas em Assassinato Jordas Golem - Eris. \n https://www.youtube.com/watch?v=N-1-DVuFaaY&index=13&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!NIDUS" in message.content.upper():
        await client.send_message(message.channel, "O diagrama do Warframe Nidus é obtido ao concluir a jornada A Jogada de Glast, e suas partes podem ser conseguidas em Oestrus - Eris. \n https://www.youtube.com/watch?v=cmw4le23JX0&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=7")

    if "!IVARA" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Ivara dropam na rotação C, em missões de Espionagem. \n https://www.youtube.com/watch?v=YWW85AfAu4k&index=8&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!NOVA" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe dropam do Raptor, em Naamah - Europa. \n https://www.youtube.com/watch?v=0GRjNrI703o&index=19&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!NYX" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Nyx dropam do inimigo Phorid, durante uma invasão infestada. \n https://www.youtube.com/watch?v=49ONrX1Xzl0&index=20&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!OCTAVIA" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Octavia dropam em Depósitos da Lua, Desafio da música, na Lua, e Sobrevivência Derelict. \n https://www.youtube.com/watch?v=v2kzd1OCHXw&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=6")

    if "!VAUBAN" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Vauban podem ser conseguidas exclusivamente em Alertas. \n https://www.youtube.com/watch?v=t6NzJewz82A&index=4&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!CHROMA" in message.content.upper():
        await client.send_message(message.channel, "O diagrama do Warframe Chroma é obtido ao concluir a jornada O Novo Estranho, e suas partes estão espalhadas pelos Terminais de Urano, Netuno e Plutão. \n https://www.youtube.com/watch?v=hPEFL0b1Drg&index=22&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!LIMBO" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Limbo são obtidas ao concluir a jornada O Teorema Limbo. \n https://www.youtube.com/watch?v=Yaj_FuKkGWM&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=5")

    if "!RHINO" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Rhino dropam do Jackal, em Fossa - Vênus. \n https://www.youtube.com/watch?v=24wDtcTwGvc&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=29")

    if "!WUKONG" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Wukong podem ser adquiridas no Laboratório Tenno, no dojo do clã. \n https://www.youtube.com/watch?v=7qKAEzRZofU&index=9&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!EQUINOX" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Equinox dropam do Tyl Regor, em Titania - Urano. \n https://www.youtube.com/watch?v=Ln-VsCtDVBU&index=29&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!INAROS" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Inaros são obtidas durante a jornada Areias de Inaros, disponível com o Baro. \n https://www.youtube.com/watch?v=pjxQLNShplU&index=28&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!BANSHEE" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Banshee podem ser adquiridas no Laboratório Tenno, no dojo do clã. \n https://www.youtube.com/watch?v=R7jPjA5il7c&index=5&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!EMBER" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Ember dropam do General Sargas Ruk, em Tethys - Saturno. \n https://www.youtube.com/watch?v=Dvc4LxOz6XM&index=24&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!LOKI" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Loki dropam das Hyena Pack, em Psamathe - Netuno. \n https://www.youtube.com/watch?v=GYvLUJG6D4c&index=14&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!FROST" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Frost dropam do Tenente Lech Kril e Capitão Vor em Exta, Ceres. \n https://www.youtube.com/watch?v=TS39p9kDO0g&index=12&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!VOLT" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Volt podem ser obtidas no Laboratório Tenno, no Dojo do clã. \n https://www.youtube.com/watch?v=w-D1NWCkHRU&index=17&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!MESA" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Mesa são obtidas no Assasinato do Mutalist Alad V - Eris, disponível após o término da jornada Paciente Zero. \n https://www.youtube.com/watch?v=-b_3Y8t8yjU&index=2&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!SARYN" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Saryn dropam de Kela De Thaym, em Merrow - Sedna. \n https://www.youtube.com/watch?v=f0Ufldkykko&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=13 ")

    if "!ZEPHYR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Zephyr podem ser obtidas no Laboratório Tenno, no Dojo do clã. \n https://www.youtube.com/watch?v=KurbStEIqrQ&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=20")

    if "!MIRAGE" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Mirage são obtidas durante a jornada Mensagens Ocultas. \n https://www.youtube.com/watch?v=j5TTRLPY8S0&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!TITANIA" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Titania são obtidas na jornada O Bosque Prateado, a quest é obtida com o líder da New Loka em qualquer Relay. \n https://www.youtube.com/watch?v=PgGy09Aomxs&index=31&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!GARA" in message.content.upper():
        await client.send_message(message.channel, "O diagrama da Gara é obtido na jornada Vigília de Saya, e seus componentes nas caçadas das Planíces de Eidolon. \n https://www.youtube.com/watch?v=UM0KhiQVOa0&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=1")

    if "!HARROW" in message.content.upper():
        await client.send_message(message.channel, "O diagrama do Harrow é obtido na Quest Correntes de Harrow, o Chassi cai de inimigos em fendas do Void, os sistemas na Rotação C de Deserção, e o neurovisor em Pago, na Fortaleza Kuva. \n https://www.youtube.com/watch?v=p2HXpeUh2QY&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=4")

    if "!NEKROS" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Nekros dropam do Lephantis, na missão de Assassinato Derelict. \n https://www.youtube.com/watch?v=NEzPyxvGLNk&index=10&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!NEZHA" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Nezha podem ser obtidas no Laboratório Tenno, no Dojo do clã. \n https://www.youtube.com/watch?v=sPkSgfenxfo&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=10")

    if "!VALKYR" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Valkyr dropam do Alad V, em Themisto - Júpiter. \n https://www.youtube.com/watch?v=x2B8d-crRZI&index=23&list=PLcHK4Prg02jdfwmrYZPG_RVGTyT2RYVPF")

    if "!TRINITY" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Trinity dropam das Ambulas, em Hades - Plutão. \n https://www.youtube.com/watch?v=KurbStEIqrQ&list=PLDmrv5FhAWj_VzURMqylYnfxlRWvtLspv&index=20")

    if "ONDE FARMA A VALKYR" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Valkyr dropam do Alad V, em Themisto - Júpiter")

    if "ONDE DROPA O HARROW" in message.content.upper():
        await client.send_message(message.channel, "O diagrama do Harrow é obtido na Quest Correntes de Harrow, o Chassi cai de inimigos em fendas do Void, os sistemas na Rotação C de Deserção, e o neurovisor em Pago, na Fortaleza Kuva")

    if "ONDE DROPA O NEKROS" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Nekros dropam do Lephantis, na missão de Assassinato Derelict")

    if "ONDE DROPA O EQUINOX" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Equinox dropam do Tyl Regor, em Titania - Urano")

    if "ONDE DROPA O ASH" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Ash dropam de inimigos Manic, que surgem em missões Grineer de alto nível")

    if "ONDE FARMA ASH" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Ash dropam de inimigos Manic, que surgem em missões Grineer de alto nível")

    if "ONDE DROPA O HYDROID" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Hydroid dropam do Vay Hek, em Oro - Terra")

    if "ONDE FARMA O ATLAS" in message.content.upper():
        await client.send_message(message.channel, "O diagrama do Warframe Atlas é obtido ao concluir a jornada O Preceito de Jordas, e suas partes podem ser conseguidas em Assassinato Jordas Golem - Eris")

    if "ONDE FARMA O NIDUS" in message.content.upper():
        await client.send_message(message.channel, "O diagrama do Warframe Nidus é obtido ao concluir a jornada A Jogada de Glast, e suas partes podem ser conseguidas em Oestrus - Eris")

    if "ONDE FARMA A IVARA" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Ivara dropam na rotação C, em missões de Espionagem")

    if "ONDE FARMA A NOVA" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe dropam do Raptor, em Naamah - Europa")

    if "ONDE FARMA A NYX" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Nyx dropam do inimigo Phorid, durante uma invasão infestada")

    if "ONDE FARMA A OCTAVIA" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Octavia dropam em Depósitos da Lua, Desafio da música, na Lua, e Sobrevivência Derelict")

    if "ONDE DROPA O VAUBAN" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Vauban podem ser conseguidas exclusivamente em Alertas")

    if "COMO PEGO O CHROMA" in message.content.upper():
        await client.send_message(message.channel, "O diagrama do Warframe Chroma é obtido ao concluir a jornada O Novo Estranho, e suas partes estão espalhadas pelos Terminais de Urano, Netuno e Plutão")

    if "ONDE FARMA O LIMBO" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Limbo são obtidas ao concluir a jornada O Teorema Limbo")

    if "ONDE FARMA O RHINO" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Rhino dropam do Jackal, em Fossa - Vênus")

    if "ONDE PEGO O WUKONG" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Wukong podem ser adquiridas no Laboratório Tenno, no dojo do clã")

    if "ONDE É QUE PEGA O EQUINOX" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Equinox dropam do Tyl Regor, em Titania - Urano")

    if "COMO QUE FARMA O INAROS" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Inaros são obtidas durante a jornada Areias de Inaros, disponível com o Baro")

    if "ONDE PEGO A BANSHEE" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Banshee podem ser adquiridas no Laboratório Tenno, no dojo do clã")

    if "ONDE FARMA A EMBER" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Ember dropam do General Sargas Ruk, em Tethys - Saturno")

    if "ONDE DROPA O LOKI" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Loki dropam das Hyena Pack, em Psamathe - Netuno")

    if "ONDE DROPA O FROST" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Frost dropam do Tenente Lech Kril e Capitão Vor em Exta, Ceres")

    if "ONDE DROPA O VOLT" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Volt podem ser obtidas no Laboratório Tenno, no Dojo do clã")

    if "ONDE FARMO A MESA" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Mesa são obtidas no Assasinato do Mutalist Alad V - Eris, disponível após o término da jornada Paciente Zero")

    if "ONDE FARMA A SARYN" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Saryn dropam de Kela De Thaym, em Merrow - Sedna")

    if "ONDE DROPA A ZEPHYR" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Zephyr podem ser obtidas no Laboratório Tenno, no Dojo do clã")

    if "ONDE DROPA A MIRAGE" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Mirage são obtidas durante a jornada Mensagens Ocultas")

    if "ONDE FARMA A TITANIA" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Titania são obtidas na jornada O Bosque Prateado, a quest é obtida com o líder da New Loka em qualquer Relay")

    if "ONDE DROPA A GARA" in message.content.upper():
        await client.send_message(message.channel, "O diagrama da Gara é obtido na jornada Vigília de Saya, e seus componentes nas caçadas das Planíces de Eidolon")

    if "ONDE QUE FARMO O HARROW" in message.content.upper():
        await client.send_message(message.channel, "O diagrama do Harrow é obtido na Quest Correntes de Harrow, o Chassi cai de inimigos em fendas do Void, os sistemas na Rotação C de Deserção, e o neurovisor em Pago, na Fortaleza Kuva")

    if "ONDE QUE DROPA O NEKROS" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Nekros dropam do Lephantis, na missão de Assassinato Derelict")

    if "ONDE FARMA O NEKROS" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Nekros dropam do Lephantis, na missão de Assassinato Derelict")
    
    if "ONDE FARMA A NEZHA" in message.content.upper():
        await client.send_message(message.channel, "As partes do Warframe Nezha podem ser obtidas no Laboratório Tenno, no Dojo do clã")

    if "ONDE DROPA A VALKYR" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Valkyr dropam do Alad V, em Themisto - Júpiter")

    if "ONDE QUE FARMA A TRINITY" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Trinity dropam das Ambulas, em Hades - Plutão")

    if "ONDE FARMA O FROST" in message.content.upper():
        await client.send_message(message.channel, "As partes da Warframe Valkyr dropam do Alad V, em Themisto - Júpiter")

    if "!ARCHWING" in message.content.upper():
        await client.send_message(message.channel, "Archwings são asas de voo Orokin usadas em missões no Espaço aberto. Para conseguir sua primeira Archwing, complete a Jornada A Archwing.")

    if "O QUE É DANO CORROSIVO" in message.content.upper():
        await client.send_message(message.channel, "Dano corrosivo (toxina + eletricidade) é um tipo de dano elemental que reduz a armadura do alvo permanentemente.")

    if "O QUE O DANO DE EXPLOSÃO FAZ" in message.content.upper():
        await client.send_message(message.channel, "O dano de explosão (fogo + frio) inflige um pequeno efeito de knockdown no alvo.")

    if "O QUE O DANO DE GÁS FAZ" in message.content.upper():
        await client.send_message(message.channel, "O dano de gás (calor + toxina) cria um efeito de veneno em área.")

    if "O QUE MAGNETISMO FAZ" in message.content.upper():
        await client.send_message(message.channel, "O dano de magnetismo (eletricidade + frio) reduz o máximo de escudos e drena energia do alvo.")

    if "O QUE RADIAÇÃO FAZ" in message.content.upper():
        await client.send_message(message.channel, "O dano de radiação (calor + eletricidade) reduz a precisão e faz com que o alvo ataque o alvo mais próximo.")

    if "O QUE É DANO VIRAL" in message.content.upper():
        await client.send_message(message.channel, "Dano viral (frio + toxina) é um tipo de dano elemental que reduz a saúde máxima do alvo")

    if "PRA QUE SERVE O DANO CORROSIVO" in message.content.upper():
        await client.send_message(message.channel, "Dano corrosivo (toxina + eletricidade) é um tipo de dano elemental que reduz a armadura do alvo permanentemente.")

    if "PRA QUE SERVE O DANO DE EXPLOSÃO" in message.content.upper():
        await client.send_message(message.channel, "O dano de explosão (fogo + frio) inflige um pequeno efeito de knockdown no alvo.")

    if "PRA QUE SERVE O DANO DE GÁS" in message.content.upper():
        await client.send_message(message.channel, "O dano de gás (calor + toxina) cria um efeito de veneno em área.")

    if "PRA QUE SERVE O DANO DE MAGNETISMO" in message.content.upper():
        await client.send_message(message.channel, "O dano de magnetismo (eletricidade + frio) reduz o máximo de escudos e drena energia do alvo.")

    if "PRA QUE SERVA O DANO DE RADIAÇÃO" in message.content.upper():
        await client.send_message(message.channel, "O dano de radiação (calor + eletricidade) reduz a precisão e faz com que o alvo ataque o alvo mais próximo.")

    if "PRA QUE SERVE O DANO VIRAL" in message.content.upper():
        await client.send_message(message.channel, "Dano viral (frio + toxina) é um tipo de dano elemental que reduz a saúde máxima do alvo")

    

    if "!CORROSIVO" in message.content.upper():
        await client.send_message(message.channel, "Dano corrosivo (toxina + eletricidade) é um tipo de dano elemental que reduz a armadura do alvo permanentemente.")

        
    if "!EXPLOSÃO" in message.content.upper():
        await client.send_message(message.channel, "O dano de explosão (fogo + frio) inflige um pequeno efeito de knockdown no alvo.")

    if "!GÁS" in message.content.upper():
        await client.send_message(message.channel, "O dano de gás (calor + toxina) cria um efeito de veneno em área.")

    if "!MAGNETISMO" in message.content.upper():
        await client.send_message(message.channel, "O dano de magnetismo (eletricidade + frio) reduz o máximo de escudos e drena energia do alvo.")

    if "!RADIAÇÃO" in message.content.upper():
        await client.send_message(message.channel, "O dano de radiação (calor + eletricidade) reduz a precisão e faz com que o alvo ataque o alvo mais próximo.")

    if "!VIRAL" in message.content.upper():
        await client.send_message(message.channel, "Dano viral (frio + toxina) é um tipo de dano elemental que reduz a saúde máxima do alvo")


    if "COMO EU UPO MAIS RÁPIDO" in message.content.upper():
        await client.send_message(message.channel, "Para subir o nível de Maestria da sua conta, é preciso que masterize (chegue ao nível 30) itens do jogo como armas e warframes.")

    if "O QUE FAÇO PRA UPAR MAIS RÁPIDO" in message.content.upper():
        await client.send_message(message.channel, "Para subir o nível de Maestria da sua conta, é preciso que masterize (chegue ao nível 30) itens do jogo como armas e warframes.")

    if "COMO EU UPO" in message.content.upper():
        await client.send_message(message.channel, "Para subir o nível de Maestria da sua conta, é preciso que masterize (chegue ao nível 30) itens do jogo como armas e warframes.")

    if "O QUE É MAESTRIA" in message.content.upper():
        await client.send_message(message.channel, "Para subir o nível de Maestria da sua conta, é preciso que masterize (chegue ao nível 30) itens do jogo como armas e warframes.")

    if "COMO É QUE FAZ PRA UPAR" in message.content.upper():
        await client.send_message(message.channel, "Para subir o nível de Maestria da sua conta, é preciso que masterize (chegue ao nível 30) itens do jogo como armas e warframes.")

    if "O QUE PRECISO FAZER PRA UPAR" in message.content.upper():
        await client.send_message(message.channel, "Para subir o nível de Maestria da sua conta, é preciso que masterize (chegue ao nível 30) itens do jogo como armas e warframes.")

    if "!CATALISADOR" in message.content.upper():
        await client.send_message(message.channel, "Catalisador Orokin é um item que duplica a capacidade de pontos de mod disponíveis em uma arma.")

    if "!REATOR" in message.content.upper():
        await client.send_message(message.channel, "Reator Orokin é um item que duplica a capacidade de pontos de mod disponíveis em um Warframe ou companheiro.")

    if "O QUE É CATALISADOR" in message.content.upper():
        await client.send_message(message.channel, "Catalisador Orokin é um item que duplica a capacidade de pontos de mod disponíveis em uma arma.")

    if "O QUE É REATOR" in message.content.upper():
        await client.send_message(message.channel, "Reator Orokin é um item que duplica a capacidade de pontos de mod disponíveis em um Warframe ou companheiro.")

    if "O QUE É UM CATALISADOR" in message.content.upper():
        await client.send_message(message.channel, "Catalisador Orokin é um item que duplica a capacidade de pontos de mod disponíveis em uma arma.")

    if "O QUE É UM REATOR" in message.content.upper():
        await client.send_message(message.channel, "Reator Orokin é um item que duplica a capacidade de pontos de mod disponíveis em um Warframe ou companheiro.")

    if "PRA QUE SERVE O CATALISADOR" in message.content.upper():
        await client.send_message(message.channel, "Catalisador Orokin é um item que duplica a capacidade de pontos de mod disponíveis em uma arma.")

    if "PRA QUE SERVE O REATOR" in message.content.upper():
        await client.send_message(message.channel, "Reator Orokin é um item que duplica a capacidade de pontos de mod disponíveis em um Warframe ou companheiro.")

    if "!FORMA" in message.content.upper():
        await client.send_message(message.channel, "Forma é um item usado para alterar a polaridade de um espaço de mod. Também pode ser utilizada para forjar itens.")

    if "O QUE É FORMA" in message.content.upper():
        await client.send_message(message.channel, "Forma é um item usado para alterar a polaridade de um espaço de mod. Também pode ser utilizada para forjar itens.")

    if "PRA QUE SERVE A FORMA" in message.content.upper():
        await client.send_message(message.channel, "Forma é um item usado para alterar a polaridade de um espaço de mod. Também pode ser utilizada para forjar itens.")

    if "SE EU COLOCAR UMA FORMA EM UMA ARMA EU GANHO MAIS XP" in message.content.upper():
        await client.send_message(message.channel, "Você só ganha xp de armas e warframes não masterizados.")

    if "SE EU COLOCAR UMA FORMA EM UMA ARMA EU GANHO XP" in message.content.upper():
        await client.send_message(message.channel, "Você só ganha xp de armas e warframes não masterizados.")

    if "SE EU COLOCAR UMA FORMA EU GANHO MAIS XP" in message.content.upper():
        await client.send_message(message.channel, "Você só ganha xp de armas e warframes não masterizados.")

    if "ONDE ACHO OS QUILS" in message.content.upper():
        await client.send_message(message.channel, "Quils será encontrado atrás desse portão: \n https://image.prntscr.com/image/Cwj0t7aaQAGIhGuZfGSHRw.png")

    if "ONDE FICA OS QUILS " in message.content.upper():
        await client.send_message(message.channel, "Quils será encontrado atrás desse portão: \n https://image.prntscr.com/image/Cwj0t7aaQAGIhGuZfGSHRw.png")

    if "ONDE TÁ OS QUILS" in message.content.upper():
        await client.send_message(message.channel, "Quils será encontrado atrás desse portão: \n https://image.prntscr.com/image/Cwj0t7aaQAGIhGuZfGSHRw.png")

    if "COMO QUE EU ACHO QUILS" in message.content.upper():
        await client.send_message(message.channel, "Quils será encontrado atrás desse portão: \n https://image.prntscr.com/image/Cwj0t7aaQAGIhGuZfGSHRw.png")

    if "ONDE ENCONTRO OS QUILS" in message.content.upper():
        await client.send_message(message.channel, "Quils será encontrado atrás desse portão: \n https://image.prntscr.com/image/Cwj0t7aaQAGIhGuZfGSHRw.png")

    if "QUEM É KONZU" in message.content.upper():
        await client.send_message(message.channel, "Konzu é um NPC encontrado em Cetus.")

    if "ONDE ENCONTRO SAYA" in message.content.upper():
        await client.send_message(message.channel, "Saya está nessa localização: \n https://image.prntscr.com/image/l8fsrv24S8qDmrX5sJX_Kw.png")

    if "ONDE É QUE TÁ A SAYA" in message.content.upper():
        await client.send_message(message.channel, "Saya está nessa localização: \n https://image.prntscr.com/image/l8fsrv24S8qDmrX5sJX_Kw.png")

    if "ONDE ENCONTRO A SAYA" in message.content.upper():
        await client.send_message(message.channel, "Saya está nessa localização: \n https://image.prntscr.com/image/l8fsrv24S8qDmrX5sJX_Kw.png")

    if "COMO QUE EU ACHO SAYA" in message.content.upper():
        await client.send_message(message.channel, "Saya está nessa localização: \n https://image.prntscr.com/image/l8fsrv24S8qDmrX5sJX_Kw.png")

    if "!SENTINELAS" in message.content.upper():
        await client.send_message(message.channel, "Sentinelas são companheiros que acompanham seus donos durante as missões. Caso morra durante a missão, o sentinela irá retornar na próxima missão normalmente.")

    if "!KUBROW" in message.content.upper():
        await client.send_message(message.channel, "Kubrows são companheiros caninos terrestres poderosos. Kubrows precisam de cuidados especiais, diferente dos sentinelas.")

    if "!KAVAT" in message.content.upper():
        await client.send_message(message.channel, "Kavats são companheiros felinos corpo a corpo, restritos ao terreno, semelhantes a Kubrows. Kavats precisam de cuidados especiais, diferente dos sentinelas.")

    if "!SINDICATOS" in message.content.upper():
        await client.send_message(message.channel, "Sindicatos são grupos que estão dispostos a ajudá-lo caso seja um membro deles. Poderá adentrar em um Sindicato com uma oferenda na aba de sindicatos, e logo depois use o seu brasão em missões, para ganhar reputação.")

    if "O QUE É SINDICATO" in message.content.upper():
        await client.send_message(message.channel, "Sindicatos são grupos que estão dispostos a ajudá-lo caso seja um membro deles. Poderá adentrar em um Sindicato com uma oferenda na aba de sindicatos, e logo depois use o seu brasão em missões, para ganhar reputação.")

    if "O QUE SÃO SINDICATOS" in message.content.upper():
        await client.send_message(message.channel, "Sindicatos são grupos que estão dispostos a ajudá-lo caso seja um membro deles. Poderá adentrar em um Sindicato com uma oferenda na aba de sindicatos, e logo depois use o seu brasão em missões, para ganhar reputação.")

    if "O QUE SÃO ESSES SINDICATOS" in message.content.upper():
        await client.send_message(message.channel, "Sindicatos são grupos que estão dispostos a ajudá-lo caso seja um membro deles. Poderá adentrar em um Sindicato com uma oferenda na aba de sindicatos, e logo depois use o seu brasão em missões, para ganhar reputação.")

    if "COMO EU EQUIPO O BRASÃO" in message.content.upper():
        await client.send_message(message.channel, "Para equipar um Brasão, vá no seu Arsenal > Aparência > Regalia.")

    if "COMO EU EQUIPO UM BRASÃO" in message.content.upper():
        await client.send_message(message.channel, "Para equipar um Brasão, vá no seu Arsenal > Aparência > Regalia.")

    if "COMO EU EQUIPO BRASÃO" in message.content.upper():
        await client.send_message(message.channel, "Para equipar um Brasão, vá no seu Arsenal > Seu Warframe > Aparência > Regalia.")

    if "COMO EU UPO UM MOD" in message.content.upper():
        await client.send_message(message.channel, "Para subir o nível do seu mod, vá em Equipamento > Mods > Clique no mod que pretende subir o nível > Iniciar Fusão.")

    if "COMO EU UPO MOD" in message.content.upper():
        await client.send_message(message.channel, "Para subir o nível do seu mod, vá em Equipamento > Mods > Clique no mod que pretende subir o nível > Iniciar Fusão.")

    if "O QUE É MOD" in message.content.upper():
        await client.send_message(message.channel, "Mods são cartas que aumentam os atributos de suas armas, warframes e companheiros.")

    if "O QUE É UM MOD" in message.content.upper():
        await client.send_message(message.channel, "Mods são cartas que aumentam os atributos de suas armas, warframes e companheiros.")

    if "O QUE SÃO MODS" in message.content.upper():
        await client.send_message(message.channel, "Mods são cartas que aumentam os atributos de suas armas, warframes e companheiros.")

    if "!MODS" in message.content.upper():
        await client.send_message(message.channel, "Mods são cartas que aumentam os atributos de suas armas, warframes e companheiros.")

    if "!ALERTAS" in message.content.upper():
        await client.send_message(message.channel, "Alertas são missões aleatórios em que você ganha prêmios especificos por concluí-las.")

    if "!AURA" in message.content.upper():
        await client.send_message(message.channel, "Mods de Aura são mods que concedem efeitos específicos diferentes dos demais mods. Mods de Aura só podem ser conseguidos em Alertas.")

    if "O QUE É MOD DE AURA" in message.content.upper():
        await client.send_message(message.channel, "Mods de Aura são mods que concedem efeitos específicos diferentes dos demais mods. Mods de Aura só podem ser conseguidos em Alertas.")

    if "COMO PEGA MOD DE AURA" in message.content.upper():
        await client.send_message(message.channel, "Mods de Aura são mods que concedem efeitos específicos diferentes dos demais mods. Mods de Aura só podem ser conseguidos em Alertas.")

    if "O QUE SÃO MODS DE AURA" in message.content.upper():
        await client.send_message(message.channel, "Mods de Aura são mods que concedem efeitos específicos diferentes dos demais mods. Mods de Aura só podem ser conseguidos em Alertas.")

    if "O QUE É AURA" in message.content.upper():
        await client.send_message(message.channel, "Mods de Aura são mods que concedem efeitos específicos diferentes dos demais mods. Mods de Aura só podem ser conseguidos em Alertas.")

    if "O QUE É UM MOD DE AURA" in message.content.upper():
        await client.send_message(message.channel, "Mods de Aura são mods que concedem efeitos específicos diferentes dos demais mods. Mods de Aura só podem ser conseguidos em Alertas.")

    if "COMO EU CONSIGO MOD DE AURA" in message.content.upper():
        await client.send_message(message.channel, "Mods de Aura são mods que concedem efeitos específicos diferentes dos demais mods. Mods de Aura só podem ser conseguidos em Alertas.")

    if "ONDE EU CONSIGO MOD DE AURA" in message.content.upper():
        await client.send_message(message.channel, "Mods de Aura são mods que concedem efeitos específicos diferentes dos demais mods. Mods de Aura só podem ser conseguidos em Alertas.")   

    if "COMO EU EQUIPO MODS" in message.content.upper():
        await client.send_message(message.channel, "Para equipar mods, vá em Equipamento > Arsenal > Arma, Warframe ou Companheiro > Aprimorar.")

    if "COMO EU EQUIPO UM MOD" in message.content.upper():
        await client.send_message(message.channel, "Para equipar mods, vá em Equipamento > Arsenal > Arma, Warframe ou Companheiro > Aprimorar.")

    if "COMO EU FAÇO PRA EQUIPAR MODS" in message.content.upper():
        await client.send_message(message.channel, "Para equipar mods, vá em Equipamento > Arsenal > Arma, Warframe ou Companheiro > Aprimorar.")

    if "COMO EU FAÇO PRA EQUIPAR UM MOD" in message.content.upper():
        await client.send_message(message.channel, "Para equipar mods, vá em Equipamento > Arsenal > Arma, Warframe ou Companheiro > Aprimorar.")

    if "COMO EU EQUIPO UM REATOR" in message.content.upper():
        await client.send_message(message.channel, "Para equipar o reator, vá em Equipamento > Arsenal > Warframe ou Companheiro > Aprimorar > Ações.")

    if "COMO EU EQUIPO UM CATALISADOR" in message.content.upper():
        await client.send_message(message.channel, "Para equipar o catalisador, vá em Equipamento > Arsenal > Arma desejada > Aprimorar > Ações.")

    if "COMO EU EQUIPO REATOR" in message.content.upper():
        await client.send_message(message.channel, "Para equipar o reator, vá em Equipamento > Arsenal > Warframe ou Companheiro > Aprimorar > Ações.")

    if "COMO EU EQUIPO CATALISADOR" in message.content.upper():
        await client.send_message(message.channel, "Para equipar o catalisador, vá em Equipamento > Arsenal > Arma desejada > Aprimorar > Ações.")

    if "COMO FAÇO PRA EQUIPAR UM REATOR" in message.content.upper():
        await client.send_message(message.channel, "Para equipar o reator, vá em Equipamento > Arsenal > Warframe ou Companheiro > Aprimorar > Ações.")

    if "COMO EU FAÇO PRA EQUIPAR UM CATALISADOR" in message.content.upper():
        await client.send_message(message.channel, "Para equipar o catalisador, vá em Equipamento > Arsenal > Arma desejada > Aprimorar > Ações.")

    if "COMO EU FAÇO TROCAS" in message.content.upper():
        await client.send_message(message.channel, "Para fazer trocas, você precisa ter pelo menos MR2. Chame a pessoa com quem deseja trocar para o seu dojo e ative a sessão de trocas, ou vá no Bazar da Maroo, em Marte.")

    if "COMO EU TROCO" in message.content.upper():
        await client.send_message(message.channel, "Para fazer trocas, você precisa ter pelo menos MR2. Chame a pessoa com quem deseja trocar para o seu dojo e ative a sessão de trocas, ou vá no Bazar da Maroo, em Marte.")

    if "COMO FAÇO TROCAS" in message.content.upper():
        await client.send_message(message.channel, "Para fazer trocas, você precisa ter pelo menos MR2. Chame a pessoa com quem deseja trocar para o seu dojo e ative a sessão de trocas, ou vá no Bazar da Maroo, em Marte.")

    if "COMO FAÇO PRA TROCAR" in message.content.upper():
        await client.send_message(message.channel, "Para fazer trocas, você precisa ter pelo menos MR2. Chame a pessoa com quem deseja trocar para o seu dojo e ative a sessão de trocas, ou vá no Bazar da Maroo, em Marte.")

    if "COMO EU FAÇO PRA TROCAR" in message.content.upper():
        await client.send_message(message.channel, "Para fazer trocas, você precisa ter pelo menos MR2. Chame a pessoa com quem deseja trocar para o seu dojo e ative a sessão de trocas, ou vá no Bazar da Maroo, em Marte.")

    if "!TROCAS" in message.content.upper():
        await client.send_message(message.channel, "Para fazer trocas, você precisa ter pelo menos MR2. Chame a pessoa com quem deseja trocar para o seu dojo e ative a sessão de trocas, ou vá no Bazar da Maroo, em Marte.")

    if "O QUE EU POSSO TROCAR" in message.content.upper():
        await client.send_message(message.channel, "Veja informações sobre trocas e o que pode ser trocado: \n https://digitalextremes.zendesk.com/hc/pt-br/articles/200092259-PERGUNTAS-FREQUENTES-SOBRE-TROCAS-DICAS-DE-TROCA-SEGURA")

    if "POSSO TROCAR PARTES" in message.content.upper():
        await client.send_message(message.channel, "Veja informações sobre trocas e o que pode ser trocado: \n https://digitalextremes.zendesk.com/hc/pt-br/articles/200092259-PERGUNTAS-FREQUENTES-SOBRE-TROCAS-DICAS-DE-TROCA-SEGURA")


    if "DÁ PRA TROCAR" in message.content.upper():
        await client.send_message(message.channel, "Veja informações sobre trocas e o que pode ser trocado: \n https://digitalextremes.zendesk.com/hc/pt-br/articles/200092259-PERGUNTAS-FREQUENTES-SOBRE-TROCAS-DICAS-DE-TROCA-SEGURA")

    if "POSSO TROCAR DIAGRAMAS" in message.content.upper():
        await client.send_message(message.channel, "Veja informações sobre trocas e o que pode ser trocado: https://digitalextremes.zendesk.com/hc/pt-br/articles/200092259-PERGUNTAS-FREQUENTES-SOBRE-TROCAS-DICAS-DE-TROCA-SEGURA")

    if "COMO EU FORJO ITENS" in message.content.upper():
        await client.send_message(message.channel, "Para forjar itens, você precisa de seu diagrama e recursos necessários. Poderá ver seus diagramas em sua Forja.")

    if "COMO QUE EU FORJO ITENS" in message.content.upper():
        await client.send_message(message.channel, "Para forjar itens, você precisa de seu diagrama e recursos necessários. Poderá ver seus diagramas em sua Forja.")

    if "COMO FORJAR ITENS" in message.content.upper():
        await client.send_message(message.channel, "Para forjar itens, você precisa de seu diagrama e recursos necessários. Poderá ver seus diagramas em sua Forja.")

    if "COMO EU JOGO NAS PLANÍCIES" in message.content.upper():
        await client.send_message(message.channel, "Para jogar nas Planícies, é preciso que chegue até Cetus, na Terra.")

    if "COMO EU JOGO MUNDO ABERTO" in message.content.upper():
        await client.send_message(message.channel, "Para jogar nas Planícies, é preciso que chegue até Cetus, na Terra.")

    if "COMO EU JOGO NO MUNDO ABERTO" in message.content.upper():
        await client.send_message(message.channel, "Para jogar nas Planícies, é preciso que chegue até Cetus, na Terra.")

    if "COMO EU JOGO NAS PLANICIES" in message.content.upper():
        await client.send_message(message.channel, "Para jogar nas Planícies, é preciso que chegue até Cetus, na Terra.")

    if "O QUE É CETUS WISP" in message.content.upper():
        await client.send_message(message.channel, "Cetus Wisp são itens raros encontrados nas Planícies.")

    if "COMO EU FARMO CETUS WISP" in message.content.upper():
        await client.send_message(message.channel, "Para farmar Cetus Wisp, veja o tutorial do youtube: \n https://www.youtube.com/watch?v=BuOx9cMoNGI.")

    if "COMO FARMA CETUS WISP" in message.content.upper():
        await client.send_message(message.channel, "Para farmar Cetus Wisp, veja o tutorial do youtube: \n https://www.youtube.com/watch?v=BuOx9cMoNGI.")

    if "ONDE EU ACHO CETUS WISP" in message.content.upper():
        await client.send_message(message.channel, "Para farmar Cetus Wisp, veja o tutorial do youtube: \n https://www.youtube.com/watch?v=BuOx9cMoNGI.")

    if "COMO EU FARMO AS RELÍQUIAS DA EMBER" in message.content.upper():
        await client.send_message(message.channel, "As relíquias da Ember, Frost e Loki Prime estão dropando exclusivamente de Pacotes de Relíquias de Sindicato e Caças de Cetus.")
        
    if "COMO EU FARMO AS RELÍQUIAS DO FROST" in message.content.upper():
        await client.send_message(message.channel, "As relíquias da Ember, Frost e Loki Prime estão dropando exclusivamente de Pacotes de Relíquias de Sindicato e Caças de Cetus.")

    if "COMO EU FARMO AS RELÍQUIAS DO LOKI" in message.content.upper():
        await client.send_message(message.channel, "As relíquias da Ember, Frost e Loki Prime estão dropando exclusivamente de Pacotes de Relíquias de Sindicato e Caças de Cetus.")

    if "ONDE FARMA AS RELÍQUIAS DA EMBER" in message.content.upper():
        await client.send_message(message.channel, "As relíquias da Ember, Frost e Loki Prime estão dropando exclusivamente de Pacotes de Relíquias de Sindicato e Caças de Cetus.")
        
    if "ONDE FARMA AS RELÍQUIAS DO FROST" in message.content.upper():
        await client.send_message(message.channel, "As relíquias da Ember, Frost e Loki Prime estão dropando exclusivamente de Pacotes de Relíquias de Sindicato e Caças de Cetus.")

    if "ONDE FARMA AS RELÍQUIAS DO LOKI" in message.content.upper():
        await client.send_message(message.channel, "As relíquias da Ember, Frost e Loki Prime estão dropando exclusivamente de Pacotes de Relíquias de Sindicato e Caças de Cetus.")    

    if "QUAIS SÃO AS RELÍQUIAS" in message.content.upper():
        await client.send_message(message.channel, "Aqui está uma lista de relíquias e seus drops: \n http://warframe.wikia.com/wiki/Void_Relic/ByRewards.")

    if "QUAL É A RELÍQUIA" in message.content.upper():
        await client.send_message(message.channel, "Aqui está uma lista de relíquias e seus drops: \n http://warframe.wikia.com/wiki/Void_Relic/ByRewards.")

    if "!RELÍQUIAS" in message.content.upper():
        await client.send_message(message.channel, "Aqui está uma lista de relíquias e seus drops: \n http://warframe.wikia.com/wiki/Void_Relic/ByRewards.")

    if "QUAIS RELÍQUIAS DROPAM" in message.content.upper():
        await client.send_message(message.channel, "Aqui está uma lista de relíquias e seus drops: \n http://warframe.wikia.com/wiki/Void_Relic/ByRewards.")

    if "QUAIS RELÍQUIAS QUE DROPAM" in message.content.upper():
        await client.send_message(message.channel, "Aqui está uma lista de relíquias e seus drops: \n http://warframe.wikia.com/wiki/Void_Relic/ByRewards.")

    if "DÁ PRA FARMAR A EMBER PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "DÁ PRA FARMAR O LOKI PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "DÁ PRA FARMAR O FROST PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "TÁ DANDO PRA FARMAR A EMBER PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")
    
    if "TÁ DANDO PRA FARMAR O LOKI PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")
    
    if "TÁ DANDO PRA FARMAR O FROST PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "DA PRA FARMAR A EMBER PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "DA PRA FARMAR O LOKI PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "DA PRA FARMAR O FROST PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "TA DANDO PRA FARMAR A EMBER PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")
    
    if "TA DANDO PRA FARMAR O LOKI PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")
    
    if "TA DANDO PRA FARMAR O FROST PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "DÁ PRA FARMAR A EMBER PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "DÁ PRA FARMAR O LOKI PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "DÁ PRA FARMAR O FROST PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")

    if "TÁ DANDO PRA FARMAR A EMBER PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")
    
    if "TÁ DANDO PRA FARMAR O LOKI PRIME" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")
    
    if "!UNVAULT" in message.content.upper():
        await client.send_message(message.channel, "Ember, Loki e Frost Prime, com seus respectivos equipamentos estão fora do vault, o que significa que suas relíquias são farmáveis.")


    if "!VAULT" in message.content.upper():
        await client.send_message(message.channel, "http://warframe.wikia.com/wiki/Prime_Vault")

    if "ONDE FARMA ENDO" in message.content.upper():
        await client.send_message(message.channel, "Endo pode ser farmado em qualquer missão, é recomendado missões infinitas.")

    if "ONDE CONSIGO ENDO" in message.content.upper():
        await client.send_message(message.channel, "Endo pode ser farmado em qualquer missão, é recomendado missões infinitas.")

    if "BOM LUGAR PRA FARMAR ENDO" in message.content.upper():
        await client.send_message(message.channel, "Endo pode ser farmado em qualquer missão, é recomendado missões infinitas.")

    if "COMO FARMA ENDO" in message.content.upper():
        await client.send_message(message.channel, "Endo pode ser farmado em qualquer missão, é recomendado missões infinitas.")

    if "ONDE EU ACHO PROSECUTOR" in message.content.upper():
        await client.send_message(message.channel, "Prosecutor é um inimigo que pode ser encontrado em missões de Ceres.")

    if "ONDE ACHO PROSECUTOR" in message.content.upper():
        await client.send_message(message.channel, "Prosecutor é um inimigo que pode ser encontrado em missões de Ceres.")

    if "ONDE ACHO O PROSECUTOR" in message.content.upper():
        await client.send_message(message.channel, "Prosecutor é um inimigo que pode ser encontrado em missões de Ceres.")

    if "O QUE É UM PROSECUTOR" in message.content.upper():
        await client.send_message(message.channel, "Prosecutor é um inimigo que pode ser encontrado em missões de Ceres.")

    if "COMO EU ACHO O PROSECUTOR" in message.content.upper():
        await client.send_message(message.channel, "Prosecutor é um inimigo que pode ser encontrado em missões de Ceres.")

    if "ONDE EU ENCONTRO O PROSECUTOR" in message.content.upper():
        await client.send_message(message.channel, "Prosecutor é um inimigo que pode ser encontrado em missões de Ceres.")

    if "!PROSECUTOR" in message.content.upper():
        await client.send_message(message.channel, "Prosecutor é um inimigo que pode ser encontrado em missões de Ceres.")

    if "ONDE EU ENCONTRO O MOD" in message.content.upper():
        await client.send_message(message.channel, "Nessa página da Wiki irá encontrar mods e suas informações: \n http://warframe.wikia.com/wiki/Mods_2.0.")

    if "ONDE DROPA O MOD" in message.content.upper():
        await client.send_message(message.channel, "Nessa página da Wiki irá encontrar mods e suas informações: \n http://warframe.wikia.com/wiki/Mods_2.0.")

    if "ONDE FARMA O MOD" in message.content.upper():
        await client.send_message(message.channel, "Nessa página da Wiki irá encontrar mods e suas informações: \n http://warframe.wikia.com/wiki/Mods_2.0.")

    if "ONDE QUE DROPA O MOD" in message.content.upper():
        await client.send_message(message.channel, "Nessa página da Wiki irá encontrar mods e suas informações: \n http://warframe.wikia.com/wiki/Mods_2.0.")

    if "ONDE EU CONSIGO O MOD" in message.content.upper():
        await client.send_message(message.channel, "Nessa página da Wiki irá encontrar o mod e suas informações: \n http://warframe.wikia.com/wiki/Mods_2.0.")

    if "COMO EU CONSIGO O MOD" in message.content.upper():
        await client.send_message(message.channel, "Nessa página da Wiki irá encontrar o mod e suas informações: \n http://warframe.wikia.com/wiki/Mods_2.0.")

    if "!FRIO" in message.content.upper():
        await client.send_message(message.channel, "Dano de frio é um tipo de dano que retarda os alvos.")

    if "!TOXINA" in message.content.upper():
        await client.send_message(message.channel, "Dano de toxina é um tipo de dano que atinge diretamente a saúde do alvo.")

    if "!ELETRICIDADE" in message.content.upper():
        await client.send_message(message.channel, "Eletricidade é um tipo de dano que causa controle em área.")

    if "!FOGO" in message.content.upper():
        await client.send_message(message.channel, "Talvez o dano elemental mais forte, o dano de fogo causa pânico e dano ao longo do tempo.")

    if "O QUE É DANO DE FRIO" in message.content.upper():
        await client.send_message(message.channel, "Dano de frio é um tipo de dano que retarda os alvos.")

    if "O QUE É DANO DE TOXINA" in message.content.upper():
        await client.send_message(message.channel, "Dano de toxina é um tipo de dano que atinge diretamente a saúde do alvo.")

    if "O QUE É DANO DE ELETRICIDADE" in message.content.upper():
        await client.send_message(message.channel, "Eletricidade é um tipo de dano que causa controle em área.")

    if "O QUE É DANO DE FOGO" in message.content.upper():
        await client.send_message(message.channel, "Talvez o dano elemental mais forte, o dano de fogo causa pânico e dano ao longo do tempo.")

    if "O QUE O DANO DE FRIO FAZ" in message.content.upper():
        await client.send_message(message.channel, "Dano de frio é um tipo de dano que retarda os alvos.")

    if "O QUE O DANO DE TOXINA FAZ" in message.content.upper():
        await client.send_message(message.channel, "Dano de toxina é um tipo de dano que atinge diretamente a saúde do alvo.")

    if "O QUE O DANO DE ELETRICIDADE FAZ" in message.content.upper():
        await client.send_message(message.channel, "Eletricidade é um tipo de dano que causa controle em área.")

    if "PRA QUE SERVE O DANO DE FOGO" in message.content.upper():
        await client.send_message(message.channel, "Talvez o dano elemental mais forte, o dano de fogo causa pânico e dano ao longo do tempo.")

    if "!CRÍTICO" in message.content.upper():
        await client.send_message(message.channel, "Dano crítico é basicamente o dano da arma multiplicado.")

    if "O QUE É DANO CRÍTICO" in message.content.upper():
        await client.send_message(message.channel, "Dano crítico é basicamente o dano da arma multiplicado.")

    if "O QUE É DANO CRITICO" in message.content.upper():
        await client.send_message(message.channel, "Dano crítico é basicamente o dano da arma multiplicado.")

    if "COMO FUNCIONA O DANO CRÍTICO" in message.content.upper():
        await client.send_message(message.channel, "Dano crítico é basicamente o dano da arma multiplicado.")

    if "!STATUS" in message.content.upper():
        await client.send_message(message.channel, "O efeito de status, também conhecido como proc, é um efeito adicional que pode ser desencadeado aleatoriamente por um golpe de uma arma.")

    if "O QUE É DANO DE STATUS" in message.content.upper():
        await client.send_message(message.channel, "O efeito de status, também conhecido como proc, é um efeito adicional que pode ser desencadeado aleatoriamente por um golpe de uma arma.")

    if "COMO FUNCIONA O DANO DE STATUS" in message.content.upper():
        await client.send_message(message.channel, "O efeito de status, também conhecido como proc, é um efeito adicional que pode ser desencadeado aleatoriamente por um golpe de uma arma.")

    if "ALGUEM ME AJUDA" in message.content.upper():
        await client.send_message(message.channel, "@here, Alguém pode ajudar ele?")

    if "ALGUÉM ME AJUDA" in message.content.upper():
        await client.send_message(message.channel, "@here, Alguém pode ajudar ele?")

    if "ALGUÉM PODE ME AJUDAR" in message.content.upper():
        await client.send_message(message.channel, "@here, Alguém pode ajudar ele?")

    if "ALGUEM PODE ME AJUDAR" in message.content.upper():
        await client.send_message(message.channel, "@here, Alguém pode ajudar ele?")

    if "ALGUEM AJUDA" in message.content.upper():
        await client.send_message(message.channel, "@here, Alguém pode ajudar ele?")

    if "ALGUÉM AJUDA" in message.content.upper():
        await client.send_message(message.channel, "@here, Alguém pode ajudar ele?")

    if "QUEM É SEU PAI" in message.content.upper():
        await client.send_message(message.channel, "Meu pai é o Jackob :heart:.")

    if "COMO EU USO O TENNO" in message.content.upper():
        await client.send_message(message.channel, "Para poder usar o Tenno, siga o tutorial: \n https://forums.warframe.com/topic/920403-tutorial-como-liberar-o-tenno/")

    if "COMO LIBERO O TENNO" in message.content.upper():
        await client.send_message(message.channel, "Para poder usar o Tenno, siga o tutorial: \n https://forums.warframe.com/topic/920403-tutorial-como-liberar-o-tenno/")

    if "COMO FAÇO PRA USAR O TENNO" in message.content.upper():
        await client.send_message(message.channel, "Para poder usar o Tenno, siga o tutorial: \n https://forums.warframe.com/topic/920403-tutorial-como-liberar-o-tenno/")

    if "PRECISO FAZER PRA USAR O TENNO" in message.content.upper():
        await client.send_message(message.channel, "Para poder usar o Tenno, siga o tutorial: \n https://forums.warframe.com/topic/920403-tutorial-como-liberar-o-tenno/")

    if "COMO LIBERA O TENNO" in message.content.upper():
        await client.send_message(message.channel, "Para poder usar o Tenno, siga o tutorial: \n https://forums.warframe.com/topic/920403-tutorial-como-liberar-o-tenno/")
    
    if "COMO USA O TENNO" in message.content.upper():
        await client.send_message(message.channel, "Para poder usar o Tenno, siga o tutorial: \n https://forums.warframe.com/topic/920403-tutorial-como-liberar-o-tenno/")

    if "COMO QUE LIBERO O TENNO" in message.content.upper():
        await client.send_message(message.channel, "Para poder usar o Tenno, siga o tutorial: \n https://forums.warframe.com/topic/920403-tutorial-como-liberar-o-tenno/")
    
    if "COMO EU FAÇO PRA USAR O TENNO" in message.content.upper():
        await client.send_message(message.channel, "Para poder usar o Tenno, siga o tutorial: \n https://forums.warframe.com/topic/920403-tutorial-como-liberar-o-tenno/")
    
    if "!ESCULTURA" in message.content.upper():
        await client.send_message(message.channel, "Escultura Ayatan é um tipo de item que pode ser usado como uma fonte de Endo ou como decoração para a sua nave de pouso.")

    if "PRA QUE SERVE ESCULTURA" in message.content.upper():
        await client.send_message(message.channel, "Escultura Ayatan é um tipo de item que pode ser usado como uma fonte de Endo ou como decoração para a sua nave de pouso.")

    if "PARA QUE SERVE ESCULTURA" in message.content.upper():
        await client.send_message(message.channel, "Escultura Ayatan é um tipo de item que pode ser usado como uma fonte de Endo ou como decoração para a sua nave de pouso.")

    if "PRA QUE SERVEM AS ESCULTURAS" in message.content.upper():
        await client.send_message(message.channel, "Escultura Ayatan é um tipo de item que pode ser usado como uma fonte de Endo ou como decoração para a sua nave de pouso.")

    if "PRA QUE SERVEM ESCULTURAS" in message.content.upper():
        await client.send_message(message.channel, "Escultura Ayatan é um tipo de item que pode ser usado como uma fonte de Endo ou como decoração para a sua nave de pouso.")

    if "O QUE SÃO ESCULTURAS" in message.content.upper():
        await client.send_message(message.channel, "Escultura Ayatan é um tipo de item que pode ser usado como uma fonte de Endo ou como decoração para a sua nave de pouso.")

    if "O QUE É ESCULTURA" in message.content.upper():
        await client.send_message(message.channel, "Escultura Ayatan é um tipo de item que pode ser usado como uma fonte de Endo ou como decoração para a sua nave de pouso.")

    if "O QUE É UMA ESCULTURA" in message.content.upper():
        await client.send_message(message.channel, "Escultura Ayatan é um tipo de item que pode ser usado como uma fonte de Endo ou como decoração para a sua nave de pouso.")

            
    if "!EXIMUS" in message.content.upper():
        await client.send_message(message.channel, "Inimigos Eximus são inimigos que possuem uma aura vermelha ao seu redor, e podem ser encontrados em qualquer missão do Sistema.")

    if "ONDE ENCONTRO EXIMUS" in message.content.upper():
        await client.send_message(message.channel, "Inimigos Eximus são inimigos que possuem uma aura vermelha ao seu redor, e podem ser encontrados em qualquer missão do Sistema.")

    if "ONDE TEM INIMIGOS EXIMUS" in message.content.upper():
        await client.send_message(message.channel, "Inimigos Eximus são inimigos que possuem uma aura vermelha ao seu redor, e podem ser encontrados em qualquer missão do Sistema.")

    if "O QUE SÃO EXIMUS" in message.content.upper():
        await client.send_message(message.channel, "Inimigos Eximus são inimigos que possuem uma aura vermelha ao seu redor, e podem ser encontrados em qualquer missão do Sistema.")

    if "O QUE SÃO INIMIGOS EXIMUS" in message.content.upper():
        await client.send_message(message.channel, "Inimigos Eximus são inimigos que possuem uma aura vermelha ao seu redor, e podem ser encontrados em qualquer missão do Sistema.")


    if "ONDE QUE TEM INIMIGOS EXIMUS" in message.content.upper():
        await client.send_message(message.channel, "Inimigos Eximus são inimigos que possuem uma aura vermelha ao seu redor, e podem ser encontrados em qualquer missão do Sistema.")

    if "ONDE ENCONTRO INIMIGOS EXIMUS" in message.content.upper():
        await client.send_message(message.channel, "Inimigos Eximus são inimigos que possuem uma aura vermelha ao seu redor, e podem ser encontrados em qualquer missão do Sistema.")

    if "COMO EU ACHO EXIMUS" in message.content.upper():
        await client.send_message(message.channel, "Inimigos Eximus são inimigos que possuem uma aura vermelha ao seu redor, e podem ser encontrados em qualquer missão do Sistema.")

    if "ONDE POSSO ENCONTRAR INIMIGOS EXIMUS" in message.content.upper():
        await client.send_message(message.channel, "Inimigos Eximus são inimigos que possuem uma aura vermelha ao seu redor, e podem ser encontrados em qualquer missão do Sistema.")

    if  "ONDE DROPA NEURODE" in message.content.upper():
        await client.send_message(message.channel, "Neurodes são recursos Raros conseguidos na Terra, Eris, Lua e Derelict")

    if "ONDE DROPA CÉLULA" in message.content.upper():
        await client.send_message(message.channel, "Célula Orokin são recursos Raros conseguidos em Saturno, Ceres, Derelict, e qualquer boss tem uma chance de dropar")

    if "ONDE DROPA MÓRFICO" in message.content.upper():
        await client.send_message(message.channel, "Mórficos são recursos Raros conseguidos em Marte, Phobos, Plutão, Europa, Mercúrio")

    if "ONDE DROPA GÁLIO" in message.content.upper():
        await client.send_message(message.channel, "Gálios são recursos raros conseguidos em Marte e Urano")

    if "ONDE DROPA TELLURIUM" in message.content.upper():
        await client.send_message(message.channel, "Tellurium são recursos raros conseguidos em Missões Archwing e Submersiveis")

    if "ONDE DROPA PLASTÍDEOS" in message.content.upper():
        await client.send_message(message.channel, "Plastídeos são recursos incomuns conseguidos em Plutão, Saturno, Eris, Urano, Phobos")

    if "ONDE DROPA NANO" in message.content.upper():
        await client.send_message(message.channel, "Nano Esporos são recursos comuns conseguidos em Eris, Derelict, Saturno, Netuno")

    if "ONDE DROPA POLÍMERO" in message.content.upper():
        await client.send_message(message.channel, "Pacotes de Polímeros são recursos incomuns conseguidos Vênus, Urano, Mercúrio")

    if "ONDE DROPA CHAPA" in message.content.upper():
        await client.send_message(message.channel, "Chapa Metálica é um recurso comum conseguido em Ceres, Sedna, Phobos, Plutão, Júpite")

    if "ONDE DROPA CIRCUITOS" in message.content.upper():
        await client.send_message(message.channel, "Circuitos são recursos incomuns conseguidos em Ceres e Vênus")

    if "ONDE DROPA CRISTAL" in message.content.upper(): 
        await client.send_message(message.channel, "Cristais de Argon são recursos raros conseguidos no Void e Alertas de Cristal Argon")

    if "ONDE DROPA MÓDULO" in message.content.upper():
        await client.send_message(message.channel, "Módulos de Controle são recursos raros conseguidos no Void, Europa, Netuno")

    if "ONDE QUE DROPA SENSOR" in message.content.upper():
        await client.send_message(message.channel, "Sensores Neurais são recursos raros conseguidos em Júpiter e Fortaleza Kuva")

    if "ONDE DROPA SENSOR" in message.content.upper():
        await client.send_message(message.channel, "Sensores Neurais são recursos raros conseguidos em Júpiter e Fortaleza Kuva")

    if "ONDE DROPA RUBEDO" in message.content.upper():
        await client.send_message(message.channel, "Rubedo é um recurso incomum conseguido na Terra, Lua, Plutão, Europa, Sedna, Phobos, Void")

    if "ONDE DROPA AMOSTRA DE FIELDRON" in message.content.upper():
        await client.send_message(message.channel, "Amostras de Fieldron são recursos de pesquisa conseguidos em Vênus, Júpiter, Marte, Europa, Netuno, Plutão")

    if "ODNE DROPA AMOSTRA DE MASSA" in message.content.upper():
        await client.send_message(message.channel, "Amostras Mutagênicas são recursos de pesquisa conseguidos em Orokin Derelict e Eris")

    if "ONDE DROPA AMPOLA" in message.content.upper():
        await client.send_message(message.channel, "Ampola de Detonite é um recurso de pesquisa conseguido em Mercúrio, Saturno, Urano, Terra, Sedna, Ceres")

    if "ONDE DROPA EXTRATO DE" in message.content.upper():
        await client.send_message(message.channel, "Extrato de Nitain é um recurso especial conseguido em Alertas, Depósitos no Void e na Lua")

    if "ONDE DROPA COORDENADAS NA" in message.content.upper():
        await client.send_message(message.channel, "Coordenadas Nav são recursos de navegação conseguidos em Containers de armazenamento em todos as missões")

    if "ONDE DROPA SYNTHULA" in message.content.upper():
        await client.send_message(message.channel, "Synthula e um recurso especial conseguido em Missões de Sobrevivência, Defesa e Interceptação em Mercurio, Vênus, Terra, Marte, Phobos, Ceres, Void")

    if "ONDE DROPA FERRITE" in message.content.upper():
        await client.send_message(message.channel, "Ferrite é um recurso comum conseguido em Mercurio, Terra, Netuno, Void")

    if "ONDE DROPA KUVA" in message.content.upper():
        await client.send_message(message.channel, "Kuva e um recurso especial conseguido em Cifões e Inundações Kuva")

    if "ONDE DROPA CRIÓTICO" in message.content.upper():
        await client.send_message(message.channel, "Criótico é um recurso incomum conseguido em Missões de escavação")

    if message.content.upper() == "!WIKIA":
        await client.send_message(message.channel, "http://warframe.wikia.com/wiki/WARFRAME_Wiki")

    if message.content.upper() == "!WIKI":
        await client.send_message(message.channel, "http://warframe.wikia.com/wiki/WARFRAME_Wiki")



 

   

   

    

    

    







    if message.content.upper().startswith('!AJUDA'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Posso lhe ajudar com locais de drop de recursos e warframes, informaçoes sobre itens do jogo, mods, etc. Caso tenha alguma dica de melhoria, fale com o Jackob." % (userID) )

        
        



























    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID) )


   

    



        
        



    
    

    

        

    
 
    

        

    


    

    

    

    


    
























    


        
        



client.run(os.environ.get("TOKEN"))
