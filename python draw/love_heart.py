from pickletools import string4
import time
import os
from time import sleep
from os import system 
import turtle as t 
a = ""
print("Can you input your name and your crush ?")
sleep(1)
you = str(input("Your Name: "))
person = str(input("That Person's Name: "))
def go_to(x, y): 
    t.up() 
    t.goto(x, y)
    t.down() 
def head(x, y, r): 
    go_to(x, y) 
    t.speed(100) 
    t.circle(r) 
    leg(x, y) 
def leg(x, y): 
    t.right(90) 
    t.forward(180) 
    t.right(30) 
    t.forward(100) 
    t.left(120) 
    go_to(x, y - 180) 
    t.forward(100) 
    t.right(120) 
    t.forward(100) 
    t.left(120) 
    hand(x, y) 
def hand(x, y): 
    go_to(x, y - 60) 
    t.forward(100) 
    t.left(60) 
    t.forward(100) 
    go_to(x, y - 90) 
    t.right(60) 
    t.forward(100) 
    t.right(60) 
    t.forward(100) 
    t.left(60) 
    eye(x, y) 
def eye(x, y): 
    go_to(x - 50, y + 130) 
    t.right(90) 
    t.forward(50) 
    go_to(x + 40, y + 130) 
    t.forward(50) 
    t.left(90) 
def big_Circle(size): 
    t.speed(100) 
    for i in range(150): 
        t.forward(size) 
        t.right(1) 
def line(size): 
    t.speed(100) 
    t.forward(51 * size) 
def small_Circle(size): 
    t.speed(100) 
    for i in range(210): 
        t.forward(size) 
        t.right(0.786) 
def heart(x, y, size): 
    go_to(x, y) 
    t.left(150) 
    t.begin_fill() 
    line(size) 
    big_Circle(size) 
    small_Circle(size) 
    t.left(120) 
    small_Circle(size) 
    big_Circle(size) 
    line(size) 
    t.end_fill() 
def main(): 
    t.pensize(2) 
    t.color('red', 'pink') 
    head(-120, 100, 100) 
    heart(250, -80, 1) 
    go_to(100, -300) 
    t.done()
main()
