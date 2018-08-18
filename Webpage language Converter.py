from tkinter import *
from bs4 import BeautifulSoup
import urllib2
from googletrans import Translator
import re


def go():
	htmltxt = urllib2.urlopen(entry.get()).read()
	soup = BeautifulSoup(htmltxt, 'lxml')
	ft = soup.find_all('p')
	tag = len(soup.find_all('p'))
	for x in range(0,tag):
		data = translator.translate(ft[x].text ,dest=option.get()).text
		text.insert(1.0, data)
		data2 = "\n\n"
		text.insert(1.0, data2)
		x=x+1


def clear():
	text.delete(1.0, END)
	

translator = Translator()

browser_window = Tk()
browser_window.geometry("1500x880")
browser_window.configure(background='#FF4500')
browser_window.title('Any website Code')
label = Label(browser_window, text= 'Enter URL:', font=("Hoefler Text", 20))
label.pack(anchor=CENTER)
label.place(height=40, width=150, x=240, y=50)
entry = Entry(browser_window, bd =5, font=("Hoefler Text", 20))
entry.place(height=40, width=700, x=420, y=50 )
button = Button(browser_window, text='Go', command = go, font=("Hoefler Text", 15))
button.pack(expand=True, fill='both')
button.place(bordermode=OUTSIDE, height=30, width=100, x=800, y=100)


button = Button(browser_window, text='Clear', command = clear, font=("Hoefler Text", 15))
button.pack(expand=True, fill='both')
button.place(bordermode=OUTSIDE, height=30, width=100, x=950, y=100)


text = Text(browser_window)
text.place(height=530, width=1200, x=100, y=150)

sList = ["af", "sq", "ar","be", "bg", "ca", "zh-CN", "zh-TW", "hr",
             "cs", "da", "nl", "en", "et", "tl", "fi", "fr", "gl", "de",
             "el", "iw", "hi", "hu", "is", "id", "ga", "it", "ja", "ko",
             "lv", "lt", "mk", "ms", "mt", "no", "fa", "pl", "pt", "ro",
             "ru", "sr", "sk", "sl", "es", "sw", "sv", "th", "tr", "uk",
             "vi", "cy", "yi"]
option = StringVar(browser_window)
option.set(sList[0])



w =OptionMenu(browser_window, option, *sList)
w.pack()
w.place(height=40,width=150, x=400, y=100)

menu = w.nametowidget(w.menuname) 
menu.configure(font=("Hoefler Text", 20))

browser_window.mainloop()