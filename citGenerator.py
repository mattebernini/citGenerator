import os
import time
import bs4 
import requests
import random
import tkinter as tk  

ora_attuale = time.strftime('%H', time.localtime())
min_attuale = time.strftime('%M', time.localtime())

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
testo = testo.replace("Ellipsis", "")
testo = testo.replace("“ —", "“\n\n —")
testo = testo.replace(",", ",\n")

# GUI 
window = tk.Tk()    #creo una finestra
window.geometry("600x300")
window.title("citGenerator")
w = tk.Label(window, text=testo)
w.pack()
w.place(relx = 0, rely = 0.3)

window.mainloop()


