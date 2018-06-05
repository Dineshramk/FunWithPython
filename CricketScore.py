import requests
from bs4 import BeautifulSoup
import tkinter as tk
import time

count = 1
while count == 1:
    source_code = requests.get("http://www.espncricinfo.com/series/8814/game/1122872/Dhaka-Division-vs-Rangpur-Division-Tier-1-national-cricket-league/")
    plain_text = source_code.text
    #print(plain_text)
    soup = BeautifulSoup(plain_text, "html.parser")
    links = set()
    for link in soup.select('head meta'):
        href1 = link.get('property')
        href2 = link.get('content')
        if (href1 is not None) and ('title' in href1):
            score = href2
        if (href1 is not None) and ('description' in href1):
            subject1 = href2
    top = tk.Tk()
    top.title(subject1)
    tk.Message(top, text=score, padx=50, pady=50).pack()
    def close_the_box():
        top.destroy()
    top.after(10000, close_the_box)
    top.mainloop()
    time.sleep(20)
    if 'Match over' in score:
        count = 0


