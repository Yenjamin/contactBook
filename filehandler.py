from collections import defaultdict
import json
import os
from tkinter import *
from tkinter import Toplevel

def readcontact():
    if os.path.exists("contacts.txt"):
        try:
            f = open("contacts.txt", "r")
            contacts = f.read()
            if contacts != "":
                f.close()
                return json.loads(contacts)
            else:
                return defaultdict(list)
        except:
            print("File Handling Error")
    else:
        return defaultdict(list)

def savecontact(contacts):
    if contacts != "":
        f = open("contacts.txt", "w+")
        a = json.dumps(contacts)
        f.write(a)
        f.close()

def exit(window):
    window.destroy()

def numbercheck(window, number):
    if len(number) != 10:
        popUp = Toplevel(window)
        popUp.geometry("300x200")
        popUp.title("error message")
        Label(popUp, text = "not the right number of digits", font="arial 6 bold",bg = "SlateGray3").place(x= 90, y=60)
        Button(popUp,text="OK", font="arial 12 bold",bg="SlateGray4", command = lambda: exit(popUp)).place(x= 130, y=80)
        return False
    return True