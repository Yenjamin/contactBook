from tkinter import *
from tkinter import scrolledtext
import filehandler

class display(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Adress Book")
        self.geometry("400x400")
        self.resizable(0,0)
        self.config(bg="SlateGray3")
        contactlist = filehandler.readcontact()
        frame = Frame(self)
        frame.pack(side = RIGHT)

        scroll = Scrollbar(frame, orient=VERTICAL)
        select = Listbox(frame, yscrollcommand=scroll.set, height=12)
        scroll.config (command=select.yview)
        scroll.pack(side=RIGHT, fill=Y)
        select.pack(side=LEFT,  fill=BOTH, expand=1)
        contact = StringVar()
        number = StringVar()
        Label(self, text = "NAME", font="arial 12 bold", bg = "SlateGray3").place(x= 30, y=20)
        Entry(self, textvariable = contact).place(x= 100, y=20)
        Label(self, text = "PHONE NO.", font="arial 12 bold",bg = "SlateGray3").place(x= 30, y=70)
        Entry(self, textvariable = number).place(x= 130, y=70)
        def selectSet() :
            select.delete(0,END)
            for name in sorted(contactlist.keys()) :
                select.insert (END, name)
        selectSet()
        def addContact(): 
            contactlist[contact.get()] = number.get()
            selectSet()
        def selected():
            index = select.curselection()[0]
            return list(sorted(contactlist.keys()))[index]
        def edit():
            contactlist[selected()] = number.get()
            contactlist[contact.get()] = contactlist.pop(selected())
            selectSet()
        def delete():
            contactlist.pop(selected())
            selectSet()
        def view():
            contact.set(selected())
            number.set(contactlist[selected()])
        def reset():
            contact.set("")
            number.set("")
        Button(self,text="ADD", font="arial 12 bold",bg="SlateGray4", command = addContact).place(x= 50, y=110)
        Button(self,text="EDIT", font="arial 12 bold",bg="SlateGray4",command = edit).place(x= 50, y=260)
        Button(self,text="DELETE", font="arial 12 bold",bg="SlateGray4",command = delete).place(x= 50, y=210)
        Button(self,text="VIEW", font="arial 12 bold",bg="SlateGray4", command = view).place(x= 50, y=160)
        Button(self,text="EXIT", font="arial 12 bold",bg="tomato", command = lambda: filehandler.exit(self)).place(x= 300, y=320)
        Button(self,text="RESET", font='arial 12 bold',bg='SlateGray4', command = reset).place(x= 50, y=310)
        self.mainloop()
        filehandler.savecontact(contactlist)