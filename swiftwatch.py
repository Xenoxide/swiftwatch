import os
import sys
import imdb
ia = imdb.IMDb()
clear = lambda: os.system('cls')
clear()
placeholder = ""
while placeholder == "":
    first = input("Made by okiedokie64. Press enter to continue or I and enter to read instructions.")
    if first == "i" or first == "I":
        clear()
        input("Created to play a movie or episode of a TV show. Supports up to 4x speed and multi-language/custom subtitles. \n\n1) Have chrome/brave or firefox with ublock origin. Not having ublock could create unwanted redirects.  \n2) Follow prompts when program starts.\n\nPress enter to continue...")
        break
    break
clear()
def checkapp():
    browser = input("Open in chrome, brave or firefox? (c/b/f)")
    bravepath = r'"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --app='
    chromepath = r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --app='
    ffcmd = 'start firefox '
    if browser == 'c' or browser == 'C':
        os.popen(chromepath + url)
    elif browser == "b" or browser == "B":
        os.popen(bravepath + url)
    elif browser == "f" or browser == "F":
        os.popen(ffcmd + url)
    else:
        input("Invalid input. Press enter to restart program.")
        os.execl(sys.executable, sys.executable, *sys.argv)
check = input("Movie or TV show? (m/t)")
if check == "m" or check == "M":
    search = input("What movie would you like to watch? \n")
    search_movie = ia.search_movie(search)
    id = search_movie[0].getID()
    url = ("https://v2.vidsrc.me/embed/tt" + str(id))
    checkapp()
    #os.popen('"C:\Program Files\Google\Chrome\Application\chrome.exe" --app=' + url)
if check == "t" or check == "T":
    search = input("What show would you like to watch?\n")
    search_movie = ia.search_movie(search)
    id = search_movie[0].getID()
    series = ia.get_movie(str(id))
    seasons = series.data['seasons']
    season = input("What season?" + str(seasons))
    ia.update(series, 'episodes')
    episodes = series.data['episodes']
    key_list = list(episodes.keys())
    key_list = str(key_list)
    episode = input("What episode? " + key_list) 
    url = ("https://v2.vidsrc.me/embed/tt" + id + "/" + season + "-" + episode)
    checkapp()
    #os.popen('"C:\Program Files\Google\Chrome\Application\chrome.exe" --app=' + url)
else: 
    input("Invalid input. Press enter to restart program.")
    os.execl(sys.executable, sys.executable, *sys.argv)
input("Press enter to quit...")
