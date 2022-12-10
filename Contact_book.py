from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
import mysql.connector
import time


root = Tk()
root.title("Contact Book")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS contact_book;")
mycursor.execute("USE contact_book;")
mycursor.execute("CREATE TABLE IF NOT EXISTS contact (name CHAR(50), phone VARCHAR(10), email VARCHAR(100));")


def AddDetails_command():
    name = Entry1.get()
    phone = Entry2.get()
    email = Entry3.get()
    if name == "" or phone == "" or email == "":
        messagebox.showerror("Error","Please enter all the details.")
    elif not phone.isdigit():
        messagebox.showerror("Error","Please enter the phone number.")
    elif len(phone)!=10:
        messagebox.showerror("Error","Please enter the correct phone number.")
    elif '@' not in email:
        messagebox.showerror("Error","Please enter the correct email.")
    else:
        mycursor.execute("INSERT INTO contact (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
        mydb.commit()
        Entry1.delete(0, END)
        Entry2.delete(0, END)
        Entry3.delete(0, END)
        messagebox.showinfo("Success", "Contact Added Successfully")

        
def ShowDetails_command():
    global row, T
    mycursor.execute("SELECT name, phone, email FROM contact")
    T = mycursor.fetchall()
    book = Tk()
    book.title('Book')
    book.resizable(width=False, height=False)
    tree = ttk.Treeview(book, column=("Name", "Phone No.", "Email"), show='headings', height=10)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Name")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Phone No.")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Email")
    for row in T:
        tree.insert('', 'end', values=row)
    tree.pack()
    book.mainloop()

bgcolor = "black"
width=224
height=205
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
root["bg"] = bgcolor

Entry1=Entry(root)
Entry1["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
Entry1["font"] = ft
Entry1["fg"] = "#333333"
Entry1["justify"] = "center"
Entry1["relief"] = "flat"
Entry1.place(x=72,y=40,width=150,height=35)

Entry2=Entry(root)
Entry2["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
Entry2["font"] = ft
Entry2["fg"] = "#333333"
Entry2["justify"] = "center"
Entry2["relief"] = "flat"
Entry2.place(x=72,y=80,width=150,height=35)

Entry3=Entry(root)
Entry3["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
Entry3["font"] = ft
Entry3["fg"] = "#333333"
Entry3["justify"] = "center"
Entry3["relief"] = "flat"
Entry3.place(x=72,y=120,width=150,height=35)

Name=Label(root)
ft = tkFont.Font(family='Times',size=10)
Name["font"] = ft
Name["fg"] = "white"
Name["justify"] = "center"
Name["text"] = "Name"
Name["bg"] = bgcolor
Name.place(x=2,y=40,width=70,height=35)

Phone_No=Label(root)
ft = tkFont.Font(family='Times',size=10)
Phone_No["font"] = ft
Phone_No["fg"] = "white"
Phone_No["justify"] = "center"
Phone_No["text"] = "Phone No."
Phone_No["bg"] = bgcolor
Phone_No.place(x=2,y=80,width=70,height=35)

Email=Label(root)
ft = tkFont.Font(family='Times',size=10)
Email["font"] = ft
Email["fg"] = "white"
Email["justify"] = "center"
Email["text"] = "Email"
Email["bg"] = bgcolor
Email.place(x=2,y=120,width=70,height=35)

Title=Label(root)
ft = tkFont.Font(family='Times',size=10)
Title["font"] = ft
Title["fg"] = "white"
Title["justify"] = "center"
Title["text"] = "Contact Book"
Title["bg"] = bgcolor
Title.place(x=2,y=0,width=220,height=35)

AddDetails=Button(root)
AddDetails["bg"] = "#1e9fff"
ft = tkFont.Font(family='Times',size=10)
AddDetails["font"] = ft
AddDetails["fg"] = "#000000"
AddDetails["justify"] = "center"
AddDetails["text"] = "Add Details"
AddDetails["relief"] = "flat"
AddDetails.place(x=1,y=170,width=110,height=35)
AddDetails["command"] = AddDetails_command

ShowDetails=Button(root)
ShowDetails["bg"] = "#009688"
ft = tkFont.Font(family='Times',size=10)
ShowDetails["font"] = ft
ShowDetails["fg"] = "#000000"
ShowDetails["justify"] = "center"
ShowDetails["text"] = "Show Details"
ShowDetails["relief"] = "flat"
ShowDetails.place(x=113,y=170,width=110,height=35)
ShowDetails["command"] = ShowDetails_command

root.mainloop()
