from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
 
root = Tk()
root.geometry("500x500+200+200")
root.title("мое окно")
 
url = "http://www.cbr.ru/scripts/XML_daily.asp?"
 
today = datetime.today()
today = today.strftime("%d/%m/%Y")
 
payload = {"date_req": today}
 
response = requests.get(url, params=payload)
 
xml = BeautifulSoup(response.content, "lxml")
 
def getCourse (id):
	return xml.find("valute",  {'id': id}).value.text

img_logo = PhotoImage(file='logo.png')
logo = Label(root, image=img_logo)
logo.place(x=0, y=0)

label1 = Label(root, text="Курс валют \n MAXIMUM банк", bg="white", fg="black")
label1.place(y=50, x=150)
 
 
def getCourse (id):
	return xml.find("valute",  {'id': id}).value.text

course = Label(root, text="Курс на: " + today.replace('/', '.'), bg="white", fg="black")
course.place(y=150, x=90)
 
course_usd = Label(root, text="$ " + getCourse("R01235"), bg="white", fg="black")
course_usd.place(y=190, x=100)
 
course_eur = Label(root, text="€ " + getCourse("R01239"), bg="white", fg="black")
course_eur.place(y=230, x=100)
 
 
root.mainloop()

