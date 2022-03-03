from collections import defaultdict
import json
import os

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