import random

lines=['top','jg','mid','sup','adc'] # NOQA
top=['Aatrox','Akali','Camille','Cassiopeia','Cho\'Gath','Darius','Dr. Mundo','Fiora','Gangplank','Garen','Gnar','Gragas','Gwen','Heimerdinger','Illaoi','Irelia','Jax','Jayce','Kalista','Karma','Kayle','Kennen','Kled','Lissandra','Lucian','Malphite','Malzahar','Maokai','Mordekaiser','Nasus','Neeko','Nocturne','Olaf','Ornn','Pantheon','Poppy','Quinn','Renekton','Rengar','Riven','Rumble','Ryze','Sejuani','Sett','Shen','Shyvana','Singed','Sion','Sylas','Tahm Kench','Teemo','Trundle','Tryndamere','Urgot','Vayne','Viego','Viktor','Vladimir','Volibear','Warwick','Wukong','Xin Zhao','Yasuo','Yone','Yorick','Zac'] # NOQA
jng=['Amumu','Cho\'Gath','Diana','Dr. Mundo','Ekko','Elise','Evelynn','Fiddlestick','Gragas','Graves','Hecarim','Ivern','Jarvan IV','Jax','Karthus','Kayn','Kha\'Zix','Kindred','Lee Sin','Lillia','Master Yi','Nasus','Nidalee','Nocturne','Nunu & Willump','Olaf','Pantheon','Poppy','Quinn','Rammus','Rek\'Sai','Rengar','Sejuani','Shaco','Shyvana','Sion','Skarner','Taliyah','Trundle','Tryndamere','Twitch','Udyr','Vi','Viego','Volibear','Warwick','Wukong','Xin Zhao','Zac'] # NOQA
mid=['Ahri','Akali','Akshan','Anivia','Annie','Aurelion Sol','Azir','Brand','Cassiopeia','Cho\'Gath','Corki','Diana','Ekko','Fizz','Galio','Gangplank','Garen','Gragas','Heimerdinger','Irelia','Jayce','Karma','Karthus','Kassadin','Katarina','Kennen','Kled','Kog\'Maw','LeBlanc','Lissandra','Lucian','Lux','Malphite','Malzahar','Morgana','Neeko','Orianna','Pantheon','Pyke','Qiyana','Renektom','Riven','Rumble','Ryze','Seraphine','Sett','Swain','Sylas','Syndra','Talon','Tristana','Twisted Fate','Veigar','Vel\'Koz','Viego','Viktor','Vladimir','Xerath','Yasuo','Yone','Zed','Ziggs','Zilean','Zoe','Zyra'] # NOQA
sup=['Alistar','Anivia','Annie','Ashe','Bard','Blitzcrank','Brand','Braum','Fiddlesticks','Galio','Gragas','Ivern','Janna','Karma','Leona','Lulu','Lux','Malphite','Maokai','Morgana','Nami','Nautilus','Neeko','Pantheon','Poppy','Pyke','Rakan','Rell','Senna','Seraphine','Sett','Shaco','Shen','Sona','Soraka','Swain','Tahm Kench','Taliyah','Taric','Teemo','Thresh','Twitch','Veigar','Vel\'Koz','Xerath','Yuumi','Zac','Ziggs','Zilean','Zyra'] # NOQA
adc=['Akshan','Aphelios','Ashe','Caitlyn','Cassiopeia','Corki','Draven','Ezreal','Heimerdinger','Jhin','Jinx','Kai\'Sa','Kalista','Kog\'Maw','Lucian','Miss Fortune','Quinn','Samira','Senna','Sivir','Tristana','Twitch','Varus','Vayne','Veigar','Xayah','Yasuo'] # NOQA


def get_responses(message: str) -> str:
    user_message = message.lower()

    if user_message in ['hello', 'hi', 'sup', 'welcome']:
        return 'Hey there'
    if user_message in ['roll', 'random']:
        return str(random.randint(1, 100))
    if user_message == 'champion top':
        return random.choice(top)
    if user_message == 'champion sup':
        return random.choice(sup)
    if user_message == 'champion adc':
        return random.choice(adc)
    if user_message == 'champion mid':
        return random.choice(mid)
    if user_message == 'champion jng':
        return random.choice(jng)
    if user_message == 'line':
        return random.choice(lines)
    if user_message in ['bye', 'cya', 'goodbye', 'ciao']:
        return 'Bye buddy it was nice to see you!'
    if user_message == 'help':
        return "`-------------------------------\n" \
               "Try one of these:\n" \
               "champion adc\n" \
               "champion sup\n" \
               "champion mid\n" \
               "champion jng\n" \
               "champion top\n" \
               "line\n" \
               "roll/random\n" \
               "'hello', 'hi', 'sup', 'welcome'\n" \
               "'bye', 'cya', 'goodbye', 'ciao'\n" \
               "horoscope + your sign\n" \
               "-------------------------------`"

    return "Repeat or try 'help. Keep in mind that everything have to be\n" \
           "in lower znaki?" # NOQA
