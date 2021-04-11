import pyttsx3
import os
from dotenv import load_dotenv
import time
import bs4 
import requests
import random

# gestione timer (woek in progress)
ora_attuale = time.strftime('%H', time.localtime())
min_attuale = time.strftime('%M', time.localtime())

load_dotenv()
ora_target = os.getenv("ORA")
min_target = os.getenv("MIN")

if int(min_attuale)%2 == 0:
    link = "https://le-citazioni.it/frasi/"
else:
    link = "https://le-citazioni.it/frasi/recente/"

# web scraping (ok)    
res = requests.get(link)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

tutte_cit = soup.find_all("h3", class_ = "blockquote-text")
tutti_autori = soup.find_all("p", class_ = "blockquote-origin")

num = random.randint(1, 16)

ancora = tutte_cit[num].find_all("a")
testo = ancora[0].get("title")
testo = testo.replace("Frase di dettaglio", "")
testo = testo.replace("“ —", "“\n\n —")
print(testo)

# speaker (ok)
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty("voice", "italian")
speaker.say(testo)
speaker.runAndWait()


