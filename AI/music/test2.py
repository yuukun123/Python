import webbrowser
import os
import smtplib

a = str(input("nhap a : "))

if "play music" in a:
    music =r"d:\code\piano.mp4"

    os.startfile(music)