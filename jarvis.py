from tkinter import *
import pyttsx3
import datetime
import time
import wikipedia
import random
import webbrowser as wb
from PIL import ImageGrab
import smtplib
import requests
import cv2
import numpy as np
import pyautogui
import psutil
import pyjokes
import re
import os
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    print(date, end=" ")
    print(month, end=" ")
    print(year)
    
    if hour >= 6 and hour < 12:
        speak("Good Morning Kislay!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Kislay!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening Kislay!")
    else:
        speak("Good Night Kislay!")
    speak("Welcome back.")
    speak("the current Time is")
    speak(Time)
    speak("the current Date is")
    speak(date)
    speak(month)
    speak(year)
    speak("Jarvis at your Service. Please tell me how can I help You?"
    speak("I can tell you today's date, current time, send email to anyone, take a screenshot, tell you CPU stats,"
    speak("update you about covid, tell you a joke, open and search chrome, search wikipedia and update you with the weather in a city. ")

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('Senderemail@gmail.com', 'MyPassword@1234')
        server.sendmail('Senderemail@gmail.com', to, content)
        server.close()
    except:
        speak("Invalid email or login credentials.")

def screenshot():
    name=random.random()
    time.sleep(5)
    img = pyautogui.screenshot()
    img.show()
    img.save("C:\\Users\\Vaibhav\\Desktop\\KISLAY\\pyproject\\Jarvis AI\\{}.png".format(name))

def cpu_stats():
    usage = str(psutil.cpu_percent())
    speak("CPU usage is "+usage+"%")
    battery=str(psutil.sensors_battery())
    speak(battery)

def jokes():
    newjoke = pyjokes.get_joke()
    print(newjoke)
    speak(newjoke)

def weather(query1):
    queryarr=query1.split()
    city=queryarr[-1]
    search="weather in "+city
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
        url="https://www.google.com/search?&q=%s"%search
        r=requests.get(url, headers=headers)
        r.raise_for_status()
        s=BeautifulSoup(r.text,"html.parser")
        temp=s.find("span", {"id": "wob_tm"})
        precip=s.find("span", {"id": "wob_pp"})
        humid=s.find("span", {"id": "wob_hm"})
        wind=s.find("span", {"id": "wob_tws"})

        temperature=str(temp)
        precipitate=str(precip)
        humidity=str(humid)
        wind_speed=str(wind)

        speak("Temperature in "+city+" is")
        speak (re.findall('\d+', temperature ))
        speak("Precipitate in percentage in " + city + " is")
        speak(re.findall('\d+', precipitate))
        speak("Humidity in percentage in " + city + " is")
        speak(re.findall('\d+', humidity))
        speak("Wind Speed in miles per hour in " + city + " is")
        speak(re.findall('\d+', wind_speed))
    except:
        print("City name not found")

def webauto():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        	"stackoverflow.com",
	        "github.com/kislay960",
	        "gmail.com",
	        "google.com",
	        "youtube.com"
    )
    for url in URLS:
        speak("opening :"+ url)
        wb.get(chrome_path).open(url)

def timefunc():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(str(Time))
    print(str(Time))

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print(date, end=" ")
    print(month,end=" ")
    print(year)
    speak("Today is ")
    speak(date)
    speak(month)
    speak(year)

def wiki(query1):
    query=query1.replace("wiki ","")
    results = wikipedia.summary(query, sentences=2)
    speak(results)
    

def search_chrome(query1):
    query = query1.replace("search chrome ","")
    speak("searching.")
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    wb.register('chrome', None, wb.BackgroundBrowser(chrome_path))
    wb.get('chrome').open_new_tab(query+'.com')

def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = r.json()
    text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'
    toast = ToastNotifier()
    speak("Please check your system's notification.")
    toast.show_toast("Covid-19 Updates",text,duration=8)

def perform():
    query=textin.get()
    if 'time' in query:
        timefunc()
    elif 'date' in query:
        date()
    elif 'wiki' in query:
        wiki(query)
    elif 'send mail' in query:
        queryarr=query.split()
        to=queryarr[3]
        content=queryarr[4:]
        sendEmail(to,content)
    elif 'screenshot' in query:
        speak("Taking screenshot")
        screenshot()
    elif 'cpu' in query:
        cpu_stats()
    elif 'joke' in query:
        jokes()
    elif 'search chrome' in query:
        search_chrome(query)
    elif 'weather' in query:
        weather(query)
    elif 'open chrome' in query:
        webauto()
    elif 'covid' in query:
        covid()
    elif 'go offline' in query:
        speak("ok sir, shutting down the system.")
        quit()
    elif 'open' in query:
        os.system('explorer C://{}'.format(query.replace('open','')))

canvas_width = 500
canvas_height = 300

win=Tk()
win.wm_title="Jarvis"

c = Canvas(win , width = canvas_width ,  height = canvas_height , background = 'deep sky blue')
c.pack()

l1 = Label(win , text='My name is Jarvis',width=20 , padx=3)
l1.place(x=180,y=10)
l2 = Label(win , text='Click the button below to get to know me better' , padx=3)
l2.place(x=125,y=40)
b1 = Button(win , text='Know Me', command=wishMe)
b1.place(x=225,y=70)
l3 = Label(win , text='How can i help you?' , padx=3)
l3.place(x=200,y=130)
textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin)
e1.place(x=165,y=160)

b1 = Button(win , text='Just this' ,command=perform)
b1.place(x=225,y=200)

win.mainloop()