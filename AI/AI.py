import time
import pyttsx3
import speech_recognition as sr
from datetime import date , datetime
import webbrowser
import wikipedia
import os
import smtplib
import sys
from random import randint
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from c import ChromeDriverManager
import json
import re
import ctypes
import time 
import psutil as ps

wikipedia.set_lang('en')

jarvis = pyttsx3.init()
voice = jarvis.getProperty('voices') #lay giong trong thu vien 
jarvis.setProperty('voice',voice[1].id)
rate = jarvis.getProperty('rate')                        
jarvis.setProperty('rate', 200)

def speak(audio):
    print('jarvis :' + audio)
    jarvis.say(audio)
    jarvis.runAndWait()
    
def name():
    speak("yes boss")
    
def clock(): #xem time 
    now = datetime.now()
    Time = now.strftime("%H:%Minutes:%p")
    speak("it is")
    speak(Time)
    
def day(): #xem day 
    day = date.today().strftime("%B %d , %Y")
    speak("today is")
    speak(day)

def order(): # su ly du lieu vao
    ear = sr.Recognizer()
    with sr.Microphone() as source:
        speak('i am listening ')
        print("i'm listening... ")
        ear.pause_threshold = 0.5
        audio = ear.listen(source)
    try:   
        boss = ear.recognize_google(audio)
        print("boss :" + boss) # type: ignore
    except :
        boss = "..."
        print('please say again')
    return boss 

def ask(): # nhan dien ngay gio va cau chao
    hour = datetime.now().hour
    if hour >=6 and hour <12 :
        speak('good morning boss ')
    elif hour >= 12 and hour <18:
        speak ('good afternoon boss ')
    else :
        speak('good evening boss ')
    speak ("i'm jarvis")
    speak ('how can i help you boss!')

def knowledge(): # wikipedia 
    try:
        speak("what you want to know")
        search = order()
        results = wikipedia.summary(search , sentences = 0 ).split('\n')
        speak(results[0])
        #speak(contents[0])
        time.sleep(2)
        for content in results[2:]:
            speak("you want know more?")
            ans = order()
            if "yes" in ans:
                speak(content)
                time.sleep(2)
            else :
                break    

        speak("thank for listen ")
    except:
        speak("i dont understand")
    
def weather(): # thoi tiet
    speak("Where do you want to see the weather?")
    time.sleep(3)
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = order().lower()
    speak(f'{city} weather is: ')
    if not city:
        pass
    api_key = "56a0f1a575f17461f37685ec84450ae3"

    call_url = url + "appid=" + api_key + "&q=" + city + "&units=metric" # type: ignore
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data['main']
        current_temp = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        sun_time  = data["sys"]
        sun_rise = datetime.now().fromtimestamp(sun_time["sunrise"])
        sun_set = datetime.now().fromtimestamp(sun_time["sunset"])
        wther = data["weather"]
        weather_des = wther[0]["description"]
        now = datetime.now()
        content = """
        today is {day} moth {month} year {year}
        sun rise at {hourrise} hour {minrise} minute
        sundown at {hourset} hour {minset} minute
        Average temperature is {temp}  °C
        The air pressure is {pressure} N/m²
        Humidity is {humidity}%
        The sky is clear today. Scattered rain is forecast in some places.""".format(day = now.day, month = now.month, year= now.year, hourrise = sun_rise.hour, minrise = sun_rise.minute,
                                                                           hourset = sun_set.hour, minset = sun_set.minute, 
                                                                           temp = current_temp, pressure = current_pressure, humidity = current_humidity)
        speak(content)
    else:
        speak("cant find city!")

def BMI(): # xem chi so va co the
    speak("this is BMI")
    while True:
        try:
            speak("Enter your height: (M) ")
            h = float(order()) # type: ignore
            he = h/100
            speak("Enter your weight: (Kg) ")
            w = float(order())
            cc = w/(he*he)
            BMI = round(cc,2)
            print("Your BMI is: " + str(BMI))
            if BMI < 16:
                speak("you are very underweight")
            elif BMI < 18.5:
                speak("you are underweight")
            elif BMI < 25:
                speak("your body is in balance")
            elif BMI < 30:
                speak("you are overweight")
            elif BMI > 30:
                speak("your body is very overweight")
            else:
                speak("sorry , i dont know")
        except:
            speak("say again!")
            
        speak("you want continue")
        an = order()    
        if "no" in an:
            speak("turn off BMI")
            break
        else:
            speak("here you are")

def game(): # game keo bua bao
    
    while True:
        try:
        #a = "Game kéo búa bao"
        #b = a.center(50)
            row_1 = '+ {:-<6} + {:-^16} + {:->6} +'.format('','','')
            row_2 = '| {:-<6} | {:-^16} | {:->6} |'.format( '','' ,'' )
            row_3 = '| {:-<6} | {:-^15} | {:->6} |'.format( '', 'GAME KEO BUA BAO' , '')
            row_4 = '| {:-<6} | {:-^16} | {:->6} |'.format( '', '', '')
            row_5 = '+ {:-<6} + {:-^16} + {:->6} +'.format('','','')
            print(row_1)
            print(row_2)
            print(row_3)
            print(row_4)
            print(row_5)

            print("\n        want out game write 'stop'")
            row_6 = '* {:-<5} | {:-^15} | {:->5} *'.format( '', 'enter bua, bao, keo' , '')
            print(row_6)
        
            player = order()
            computer = randint(1,3)
            if  "stop" in player :
                print("see ya")
                break	
        
            if computer == 1:
                computer = "hammer"
            if computer == 2:
                computer = "paper"
            if computer == 3:
                computer = "scissors"

            print("___")
            print("your choose: " + player)
            print("computer choose: " + str(computer))
            print("___")

            if player == computer:
                print("draw")

            else :
                if player == "scissors":
                    if computer == "hammer":
                        print("loser")
                    else: 
                        print("win")
                            
                elif player == "hammer":
                    if computer == "scissors":
                        print("win")
                    else: print("loser")
                    
                elif player == "paper":
                    if computer == "scissors":
                        print("loser")
                    else: print("win")
                else: print("write wrong \n ")
                
        except:
            speak("wrong")
            
def ram(): #xem cpu may
    def display_usage (cpu_usage, mem_usage, bars = 50):
        cpu_percent = (cpu_usage / 100.0)
        cpu_bar = (cpu_percent * bars ) + (bars - int(cpu_percent * bars))
        
        mem_percent = (mem_usage/ 100.0)
        mem_bar = int(mem_percent * bars) +  (bars - int(mem_percent *bars))
        
        speak(f"\nCPU Usage: {cpu_usage: .2f}% ")
        speak(f"MEM Usage:  {mem_usage: .2f}% "  )
        
    while True:
        display_usage(ps.cpu_percent(), ps.virtual_memory().percent, 30)
        time.sleep(0.5)
        r = order()
        if "stop" in r:
            speak("out cpu")
            break 
        
def disk():
    while True:
        hd = ps.disk_usage('/')
        speak("your disk'D' has")
        speak(f"total: {hd.total / 1024**3}")
        speak(f'used: {hd.used / 1024**3}')
        speak(f'free: {hd.free / 1024**3}')
        re = order()
        if "stop" in re:
            speak("out disk")
            break
        


                
def stop(): # dung AI
    speak("i'm  sleeping. Goodbye boss")
    
if __name__=="__main__":
    ask()
    
    while True:
        boss=order().lower()
        
        if "jarvis" in boss:
            name()
        elif "google" in boss :
            speak("What should I search,boss")
            search=order().lower()
            url = f"https://google.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f'Here is your {search} on google')
        elif "youtube" in boss :
            speak("What should I search,boss")
            search=order().lower()
            url = f"https://www.youtube.com/={search}"
            webbrowser.get().open(url)
            speak(f'Here is your {search} on youtube')
        # elif "open video" in boss:
        #     video =r"Downloads\piano.mp4"
        #     os.startfile(video)
        elif "time" in boss :
            clock()
        elif "day" in boss :
            day()
        elif "wikipedia" in boss :
            knowledge()
        elif "weather" in boss:
            weather()
        elif "BMI" in boss :
            BMI()
        elif "game on" in boss:
            game()
        elif "cpu" in boss:
            ram()    
        elif "check" in boss:
            disk()
        
        elif "turn off" in boss:
            stop()
            break