import requests
from bs4 import BeautifulSoup
import tkinter as tk
import time

count = 1
while count == 1:
    source_code = requests.get("http://www.espncricinfo.com/west-indies-v-afghanistan-2017/engine/match/1089778.html")
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    links = set()
    for link in soup.select('head meta'):
        href1 = link.get('property')
        href2 = link.get('content')
        if (href1 is not None) and ('title' in href1):
            score = href2
        if (href1 is not None) and ('description' in href1):
            subject = href2
    top = tk.Tk()
    top.title(subject)
    tk.Message(top, text=score, padx=50, pady=50).pack()
    def close_the_box():
        top.destroy()
    top.after(3000, close_the_box)
    top.mainloop()
    time.sleep(100)
    if 'Match over' in score:
        count = 0


